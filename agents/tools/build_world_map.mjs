// build_world_map.mjs — generator for web/src/data/world-map.json (2026-11-26).
//
// The /map/ pages draw every country as an inline SVG path, projected here once,
// so the served page fetches nothing from any map service (qa_third_party_origins).
// It is a GENERATOR, not an assertion: no qa_ prefix, outside the counting glob.
//
// Source: Natural Earth via the world-atlas package (public domain), 110m for the
// whole world, with 50m shapes for the small countries 110m drops (Bahrain,
// Singapore, Mauritius and similar). Projection: Natural Earth 1, Antarctica left out.
//
// Regenerate (dependencies are installed outside the repository on purpose, so the
// site's lockfile and CI install do not change):
//   mkdir -p /tmp/geo && cd /tmp/geo && npm i world-atlas@2 topojson-client@3 d3-geo@3
//   NODE_PATH=/tmp/geo/node_modules node agents/tools/build_world_map.mjs /tmp/geo web/src/data/world-map.json
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const [geoDir, out] = process.argv.slice(2);
const require = createRequire(path.join(geoDir, 'node_modules', 'x.js'));
const { feature } = require('topojson-client');
const { geoNaturalEarth1, geoPath, geoArea, geoGraticule } = require('d3-geo');
const atlas = (res) => JSON.parse(fs.readFileSync(path.join(geoDir, 'node_modules/world-atlas', `countries-${res}.json`)));

const W = 1000;
const t110 = atlas('110m');
const t50 = atlas('50m');
const f110 = feature(t110, t110.objects.countries).features.filter((f) => f.properties.name !== 'Antarctica');
const have = new Set(f110.map((f) => f.id));
const f50extra = feature(t50, t50.objects.countries).features.filter(
  (f) => f.id && !have.has(f.id) && f.properties.name !== 'Antarctica' && geoArea(f) > 0,
);
const all = [...f110, ...f50extra];
const fc = { type: 'FeatureCollection', features: all };
const proj = geoNaturalEarth1().fitWidth(W, fc);
const p = geoPath(proj).digits(1);
const [[, y0], [, y1]] = p.bounds(fc);
const H = Math.ceil(y1 - y0 + 2);
proj.translate([proj.translate()[0], proj.translate()[1] - y0 + 1]);

const countries = all
  .map((f) => {
    const d = p(f);
    if (!d) return null;
    const [[x0, yy0], [x1, yy1]] = p.bounds(f);
    const [cx, cy] = p.centroid(f);
    return {
      id: String(f.id ?? f.properties.name),
      name: f.properties.name,
      d,
      cx: Math.round(cx * 10) / 10,
      cy: Math.round(cy * 10) / 10,
      // A country smaller than about 6 x 6 px at this width cannot be clicked, so the
      // page draws a marker over it as well.
      small: (x1 - x0) * (yy1 - yy0) < 36,
    };
  })
  .filter(Boolean)
  .sort((a, b) => a.id.localeCompare(b.id));

fs.mkdirSync(path.dirname(out), { recursive: true });
// The globe's outline and a 20-degree graticule, both clipped by the projection itself.
const sphere = p({ type: 'Sphere' });
const graticule = p(geoGraticule().step([20, 20])());
fs.writeFileSync(out, JSON.stringify({ width: W, height: H, source: 'Natural Earth (public domain), via world-atlas 2', sphere, graticule, countries }) + '\n');
console.log(`wrote ${countries.length} countries, ${W}x${H}, ${fs.statSync(out).size} bytes, ${f50extra.length} from 50m`);

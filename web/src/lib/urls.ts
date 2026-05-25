/**
 * URL helper that prepends `import.meta.env.BASE_URL` to absolute site paths
 * so the build resolves correctly under a non-root base (e.g. /madar/).
 *
 * Usage:
 *   import { withBase } from '../lib/urls';
 *   <a href={withBase('/about/')}>About</a>
 *   <img src={withBase(`/stills/${slug}.svg`)} />
 *
 * For external URLs (http/https/mailto/etc.) and protocol-relative URLs,
 * the input is returned unchanged.
 */
export function withBase(path: string): string {
  if (!path) return path;
  // Pass through external/protocol-relative/anchor/mailto/tel URLs untouched.
  if (/^(?:[a-z][a-z0-9+.-]*:|\/\/|#)/i.test(path)) return path;
  const base = import.meta.env.BASE_URL || '/'; // normalized; usually ends with '/'
  if (!path.startsWith('/')) {
    // Treat as relative to base.
    return base + path;
  }
  // base ends with '/', path starts with '/'; strip one to avoid '//'.
  return base.replace(/\/$/, '') + path;
}

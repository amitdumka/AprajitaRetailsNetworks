import { test as test$1 } from '@playwright/test';
export { expect } from '@playwright/test';
import { e as createTest, w as waitForHydration } from './shared/test-utils.B57u8E0c.mjs';
import 'node:path';
import 'defu';
import 'consola';
import 'node:fs';
import '@nuxt/kit';
import { d as url } from './shared/test-utils.BegIhSnH.mjs';
import 'pathe';
import 'node:url';
import 'execa';
import 'get-port-please';
import 'ofetch';

{
  if (process.env.TEST_WORKER_INDEX) {
    for (const stream of [process.stdout, process.stderr]) {
      if (!stream.clearLine) {
        stream.clearLine = (dir, callback) => {
          callback?.();
          return true;
        };
      }
      if (!stream.cursorTo) {
        stream.cursorTo = (x, y, callback) => {
          if (callback)
            callback();
          else if (y instanceof Function)
            y();
          return true;
        };
      }
    }
  }
}
const test = test$1.extend({
  nuxt: [void 0, { option: true, scope: "worker" }],
  _nuxtHooks: [
    async ({ nuxt }, use) => {
      const hooks = createTest(nuxt || {});
      await hooks.setup();
      await use(hooks);
      await hooks.afterAll();
    },
    { scope: "worker" }
  ],
  baseURL: async ({ _nuxtHooks }, use) => {
    _nuxtHooks.beforeEach();
    await use(url("/"));
    _nuxtHooks.afterEach();
  },
  goto: async ({ page }, use) => {
    await use(async (url2, options) => {
      const waitUntil = options?.waitUntil;
      if (waitUntil && ["hydration", "route"].includes(waitUntil)) {
        delete options.waitUntil;
      }
      const response = await page.goto(url2, options);
      await waitForHydration(page, url2, waitUntil);
      return response;
    });
  }
});

export { test };

import { Browser, BrowserContextOptions, Page, Response, LaunchOptions } from 'playwright-core';
import { NuxtConfig, Nuxt } from '@nuxt/schema';
import { ExecaChildProcess } from 'execa';

declare function createBrowser(): Promise<void>;
declare function getBrowser(): Promise<Browser>;
type _GotoOptions = NonNullable<Parameters<Page['goto']>[1]>;
interface GotoOptions extends Omit<_GotoOptions, 'waitUntil'> {
    waitUntil?: 'hydration' | 'route' | _GotoOptions['waitUntil'];
}
interface NuxtPage extends Omit<Page, 'goto'> {
    goto: (url: string, options?: GotoOptions) => Promise<Response | null>;
}
declare function createPage(path?: string, options?: BrowserContextOptions): Promise<NuxtPage>;
declare function waitForHydration(page: Page, url: string, waitUntil?: GotoOptions['waitUntil']): Promise<void>;

type TestRunner = 'vitest' | 'jest' | 'cucumber';
interface TestOptions {
    testDir: string;
    fixture: string;
    configFile: string;
    rootDir: string;
    buildDir: string;
    nuxtConfig: NuxtConfig;
    build: boolean;
    dev: boolean;
    setupTimeout: number;
    waitFor: number;
    browser: boolean;
    runner: TestRunner;
    logLevel: number;
    browserOptions: {
        type: 'chromium' | 'firefox' | 'webkit';
        launch?: LaunchOptions;
    };
    server: boolean;
    port?: number;
}
interface TestContext {
    options: TestOptions;
    nuxt?: Nuxt;
    browser?: Browser;
    url?: string;
    serverProcess?: ExecaChildProcess;
    mockFn?: Function;
    /**
     * Functions to run on the vitest `afterAll` hook.
     * Useful for removing anything created during the test.
     */
    teardown?: (() => void)[];
}
interface TestHooks {
    beforeEach: () => void;
    afterEach: () => void;
    afterAll: () => Promise<void>;
    setup: () => Promise<void>;
    ctx: TestContext;
}

export { type GotoOptions as G, type TestOptions as T, type TestContext as a, type TestHooks as b, createBrowser as c, createPage as d, type TestRunner as e, getBrowser as g, waitForHydration as w };

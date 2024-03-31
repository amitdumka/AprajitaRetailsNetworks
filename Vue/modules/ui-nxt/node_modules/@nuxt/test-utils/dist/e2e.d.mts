import { T as TestOptions, a as TestContext, b as TestHooks } from './shared/test-utils.9059LSjm.mjs';
export { G as GotoOptions, e as TestRunner, c as createBrowser, d as createPage, g as getBrowser, w as waitForHydration } from './shared/test-utils.9059LSjm.mjs';
import { FetchOptions } from 'ofetch';
import 'playwright-core';
import '@nuxt/schema';
import 'execa';

declare function createTestContext(options: Partial<TestOptions>): TestContext;
declare function useTestContext(): TestContext;
declare function setTestContext(context: TestContext): TestContext;
declare function setTestContext(context?: TestContext): TestContext | undefined;
declare function isDev(): boolean;
declare function recoverContextFromEnv(): void;
declare function exposeContextToEnv(): void;

declare function mockFn(): Function | undefined;
declare function mockLogger(): Record<string, Function>;

declare function loadFixture(): Promise<void>;
declare function buildFixture(): Promise<void>;

interface StartServerOptions {
    env?: Record<string, unknown>;
}
declare function startServer(options?: StartServerOptions): Promise<void>;
declare function stopServer(): Promise<void>;
declare function fetch(path: string, options?: any): Promise<Response>;
declare function $fetch(path: string, options?: FetchOptions): Promise<any>;
declare function url(path: string): string;

declare function setupCucumber(hooks: TestHooks): Promise<void>;

declare function setupJest(hooks: TestHooks): Promise<void>;

declare function setupVitest(hooks: TestHooks): Promise<void>;

declare const setupMaps: {
    cucumber: typeof setupCucumber;
    jest: typeof setupJest;
    vitest: typeof setupVitest;
};
declare function createTest(options: Partial<TestOptions>): TestHooks;
declare function setup(options?: Partial<TestOptions>): Promise<void>;

interface RunTestOptions {
    rootDir: string;
    dev?: boolean;
    watch?: boolean;
    runner?: 'vitest';
    globalSetup?: boolean;
}
declare function runTests(opts: RunTestOptions): Promise<void>;

export { $fetch, type RunTestOptions, type StartServerOptions, TestContext, TestHooks, TestOptions, buildFixture, createTest, createTestContext, exposeContextToEnv, fetch, isDev, loadFixture, mockFn, mockLogger, recoverContextFromEnv, runTests, setTestContext, setup, setupMaps, startServer, stopServer, url, useTestContext };

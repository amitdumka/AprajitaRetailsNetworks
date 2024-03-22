/** @type { import('@storybook/react-vite').StorybookConfig } */
const config = {
  stories: ["../src/**/*.mdx", "../src/**/*.stories.@(js|jsx|mjs|ts|tsx)"],
  addons: [
    "@storybook/addon-links",
    "@storybook/addon-essentials",
    "@storybook/addon-onboarding",
    "@storybook/addon-interactions",
    '@storybook/addon-google-analytics',
    'storybook-dark-mode',
    "storybook-addon-preview/register",
    "@storybook/addon-themes",
    'storybook-addon-custom-event-broadcaster',
    "storybook-addon-playground",
    'storybook-addon-live-examples',
    'storybook-addon-swc',
    '@stackblitz/storybook-addon-stackblitz',
    '@storybook/addon-actions',
    '@storybook/addon-controls'
  ],
  framework: {
    name: "@storybook/react-vite",
    options: {},
  },
  docs: {
    autodocs: "tag",
  },
};
export default config;

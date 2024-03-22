/**
=========================================================
* Aprajita Retails -Networks   React - v3.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/soft-ui-dashboard-pro-react
* Copyright 2024 Amit Kumar (AKS Labs(India))

Coded by Amit Kumar

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// Aprajita Retails -Networks   React base styles
import colors from "assets/theme/base/colors";

// Aprajita Retails -Networks   React helper functions
import pxToRem from "assets/theme/functions/pxToRem";

const { transparent } = colors;

const stepper = {
  styleOverrides: {
    root: {
      margin: `${pxToRem(48)} 0`,
      padding: `0 ${pxToRem(12)}`,

      "&.MuiPaper-root": {
        backgroundColor: transparent.main,
      },
    },
  },
};

export default stepper;

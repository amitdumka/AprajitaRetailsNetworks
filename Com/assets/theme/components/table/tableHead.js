/**
=========================================================
* Aprajita Retails -Networks  - v3.1.0
=========================================================

* Product Page: https://www.creative-tim.com/product/soft-ui-dashboard-pro-react
* Copyright 2024 Amit Kumar (AKS Lab (India))

Code by Amit Kumar

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// Aprajita Retails -Networks  base styles
import borders from "assets/theme/base/borders";

// Aprajita Retails -Networks  helper functions
import pxToRem from "assets/theme/functions/pxToRem";

const { borderRadius } = borders;

const tableHead = {
  styleOverrides: {
    root: {
      display: "block",
      padding: `${pxToRem(16)} ${pxToRem(16)} 0  ${pxToRem(16)}`,
      borderRadius: `${borderRadius.xl} ${borderRadius.xl} 0 0`,
    },
  },
};

export default tableHead;

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
import typography from "assets/theme/base/typography";
import colors from "assets/theme/base/colors";

// Aprajita Retails -Networks  helper functions
import pxToRem from "assets/theme/functions/pxToRem";

const { size, fontWeightRegular } = typography;
const { grey, dark, secondary } = colors;

const stepLabel = {
  styleOverrides: {
    label: {
      marginTop: `${pxToRem(8)} !important`,
      fontWeight: fontWeightRegular,
      fontSize: size.md,
      color: grey[300],

      "&.Mui-active": {
        fontWeight: `${fontWeightRegular} !important`,
        color: `${dark.main} !important`,
      },

      "&.Mui-completed": {
        fontWeight: `${fontWeightRegular} !important`,
        color: `${secondary.main} !important`,
      },
    },
  },
};

export default stepLabel;

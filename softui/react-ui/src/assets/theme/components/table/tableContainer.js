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
import boxShadows from "assets/theme/base/boxShadows";
import borders from "assets/theme/base/borders";

const { white } = colors;
const { xxl } = boxShadows;
const { borderRadius } = borders;

const tableContainer = {
  styleOverrides: {
    root: {
      backgroundColor: white.main,
      boxShadow: xxl,
      borderRadius: borderRadius.xl,
    },
  },
};

export default tableContainer;

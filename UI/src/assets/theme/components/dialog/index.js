/**
=========================================================
* Aprajita Retails Dashboard - v3.1.0
=========================================================

* Product Page: https://www.aprajitaretails.in/amitkumar/product/soft-ui-dashboard-pro-react
* Copyright 2023 Amit Kumar (https://www.aprajitaretails.in/amitkumar)

Coded by Amit Kumar (www.aprajitaretails.in/amitkumar)

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// Aprajita Retails Dashboard base styles
import borders from "assets/theme/base/borders";
import boxShadows from "assets/theme/base/boxShadows";

const { borderRadius } = borders;
const { xxl } = boxShadows;

const dialog = {
  styleOverrides: {
    paper: {
      borderRadius: borderRadius.lg,
      boxShadow: xxl,
    },

    paperFullScreen: {
      borderRadius: 0,
    },
  },
};

export default dialog;

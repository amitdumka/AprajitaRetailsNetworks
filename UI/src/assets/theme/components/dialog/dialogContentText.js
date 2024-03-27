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
import typography from "assets/theme/base/typography";
import colors from "assets/theme/base/colors";

// Aprajita Retails Dashboard helper functions
// import pxToRem from "assets/theme/functions/pxToRem";

const { size } = typography;
const { text } = colors;

const dialogContentText = {
  styleOverrides: {
    root: {
      fontSize: size.md,
      color: text.main,
    },
  },
};

export default dialogContentText;

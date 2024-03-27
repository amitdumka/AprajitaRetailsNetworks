/**
=========================================================
* Aprajita Retails Dashboard - v1.0.1
=========================================================

* Product Page: https://www.aprajitaretails.in/amitkumar/product/soft-ui-dashboard-react
* Copyright 2023 Amit Kumar (https://www.aprajitaretails.in/amitkumar)

Coded by Amit Kumar (www.aprajitaretails.in/amitkumar)

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { forwardRef } from "react";

// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// Custom styles for SoftAvatar
import SoftAvatarRoot from "components/SoftAvatar/SoftAvatarRoot";

const SoftAvatar = forwardRef(({ bgColor, size, shadow, ...rest }, ref) => (
  <SoftAvatarRoot ref={ref} ownerState={{ shadow, bgColor, size }} {...rest} />
));

// Setting default values for the props of SoftAvatar
SoftAvatar.defaultProps = {
  bgColor: "transparent",
  size: "md",
  shadow: "none",
};

// Typechecking props for the SoftAvatar
SoftAvatar.propTypes = {
  bgColor: PropTypes.oneOf([
    "transparent",
    "primary",
    "secondary",
    "info",
    "success",
    "warning",
    "error",
    "light",
    "dark",
  ]),
  size: PropTypes.oneOf(["xs", "sm", "md", "lg", "xl", "xxl"]),
  shadow: PropTypes.oneOf(["none", "xs", "sm", "md", "lg", "xl", "xxl", "inset"]),
};

export default SoftAvatar;

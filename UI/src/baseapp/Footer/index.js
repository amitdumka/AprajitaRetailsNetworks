/**
=========================================================
* Aprajita Retails Dashboard - v1.0.1
=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// @mui material components
import Link from "@mui/material/Link";
import Icon from "@mui/material/Icon";

// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Aprajita Retails Dashboard base styles
import typography from "assets/theme/base/typography";

function Footer({ company, links, fixedFooter }) {
  const { href, name } = company;
  const { size } = typography;
  let position = "fixed";
  if (fixedFooter) {
    position = "fixed";
  } else {
    position = "absolute";
  }
  const renderLinks = () =>
    links.map((link) => (
      <SoftBox key={link.name} component="li" px={2} lineHeight={1}>
        <Link href={link.href} target="_blank">
          <SoftTypography variant="button" fontWeight="regular" color="text">
            {link.name}
          </SoftTypography>
        </Link>
      </SoftBox>
    ));

  return (
    <SoftBox
      component="footer"
      borderRadius="xl"
      bgColor="white"
      width="80%"
      display="flex"
      flexDirection={{ xs: "column", lg: "row" }}
      justifyContent="space-between"
      alignItems="center"
      position={position}
      px={1.5}
      sx={{
        
        bottom: 10, // And this
      }}
    >
      <SoftBox
        display="flex"
        justifyContent="center"
        alignItems="center"
        flexWrap="wrap"
        color="text"
        fontSize={size.sm}
        px={1.5}
      >
        &copy; {new Date().getFullYear()}, build by
        {/* <SoftBox fontSize={size.md} color="text" mb={-0.5} mx={0.25}>
          <Icon color="inherit" fontSize="inherit">
            favorite
          </Icon>
        </SoftBox> */}
        <Link href={href} target="_blank">
          <SoftTypography variant="button" fontWeight="medium">
            &nbsp;{name}&nbsp;
          </SoftTypography>
        </Link>
        for Aprajita Retails.
      </SoftBox>
      <SoftBox
        component="ul"
        sx={({ breakpoints }) => ({
          display: "flex",
          flexWrap: "wrap",
          alignItems: "center",
          justifyContent: "center",
          listStyle: "none",
          mt: 3,
          mb: 0,
          p: 0,

          [breakpoints.up("lg")]: {
            mt: 0,
          },
        })}
      >
        {renderLinks()}
      </SoftBox>
    </SoftBox>
  );
}

// Setting default values for the props of Footer
Footer.defaultProps = {
  company: { href: "https://www.aprajitaretails.in/", name: "Amit Kumar" },
  links: [
    { href: "https://www.aprajitaretails.in/amitkumar/", name: "Amit Kumar" },
    { href: "https://www.aprajitaretails.in/aboutus", name: "About Us" },
    { href: "https://www.aprajitaretails.in/contactus", name: "Contact Us" },
    { href: "https://www.aprajitaretails.in/amitkumar/stores", name: "Stores" },
  ],
  fixedFooter:true,
};

// Typechecking props for the Footer
Footer.propTypes = {
  company: PropTypes.objectOf(PropTypes.string),
  links: PropTypes.arrayOf(PropTypes.object),
  fixedFooter: PropTypes.bool,
};

export default Footer;

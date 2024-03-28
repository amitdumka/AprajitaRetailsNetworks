/**
 * Sidebar navigation component
 *              It will be used for nested Navigation
 *
 * Author: Amit Kumar
 * Date : 27/03/2024
 */
import { useEffect } from "react";

// react-router-dom components
import { useLocation, NavLink } from "react-router-dom";

// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";

// @mui material components
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import Link from "@mui/material/Link";
import Icon from "@mui/material/Icon";

// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
import SoftButton from "components/SoftButton";

// Custom styles for the Sidenav
import SidebarRoot from "baseapp/SideBar/SidebarRoot";
import SidebarCollapse from "baseapp/SideBar/SidebarCollapse";
import NestedSidebarItem from "baseapp/SideBar/NestedSidebarItem";
import sidenavLogoLabel from "baseapp/Sidenav/styles/sidenav";

// Aprajita Retails Dashboard context
import { useSoftUIController, setMiniSidenav } from "context";

function Sidebar({ color, brand, brandName, routes, ...rest }) {
  const [controller, dispatch] = useSoftUIController();
  const { miniSidenav, transparentSidenav } = controller;
  const location = useLocation();
  const { pathname } = location;
  const collapseName = pathname.split("/").slice(1)[0];
  const nestedCollapseName = pathname.split("/").slice(1)[1];

  const closeSidenav = () => setMiniSidenav(dispatch, true);
  useEffect(() => {
    // A function that sets the mini state of the sidenav.
    function handleMiniSidenav() {
      setMiniSidenav(dispatch, window.innerWidth < 1200);
    }

    /** 
     The event listener that's calling the handleMiniSidenav function when resizing the window.
    */
    window.addEventListener("resize", handleMiniSidenav);

    // Call the handleMiniSidenav function to set the state with the initial value.
    handleMiniSidenav();

    // Remove event listener on cleanup
    return () => window.removeEventListener("resize", handleMiniSidenav);
  }, [dispatch, location]);

  // Render all the routes from the routes.js (All the visible items on the Sidenav)
  const renderRoutes = routes.map(
    ({ type, name, icon, title, noCollapse, collapse, key, route, href }) => {
      let returnValue;
      //console.log(type, name, key, route,collapseName);
      if (type === "collapse") {
        returnValue = href ? (
          <Link
            href={href}
            key={key}
            target="_blank"
            rel="noreferrer"
            sx={{ textDecoration: "none" }}
          >
            <SidebarCollapse
              color={color}
              name={name}
              icon={icon}
              active={key === collapseName}
              noCollapse={noCollapse}
            />
          </Link>
        ) : (
          <>
            <NestedSidebarItem
              color={color}
              key={key}
              name={name}
              icon={icon}
              active={key === collapseName}
              noCollapse={noCollapse}
              collapse={collapse}
              route={route}
              href={href}
              title={title}
              collapseName={collapseName}
              nestedCollapseName={nestedCollapseName}
            />
          </>
        );
      } else if (type === "title") {
        returnValue = (
          <SoftTypography
            key={key}
            display="block"
            variant="caption"
            fontWeight="bold"
            textTransform="uppercase"
            opacity={0.6}
            pl={3}
            mt={2}
            mb={1}
            ml={1}
          >
            {title}
          </SoftTypography>
        );
      } else if (type === "divider") {
        returnValue = <Divider key={key} />;
      }

      return returnValue;
    }
  );

  return (
    <SidebarRoot {...rest} variant="permanent" ownerState={{ transparentSidenav, miniSidenav }}>
      <SoftBox pt={3} pb={1} px={4} textAlign="center">
        <SoftBox
          display={{ xs: "block", xl: "none" }}
          position="absolute"
          top={0}
          right={0}
          p={1.625}
          onClick={closeSidenav}
          sx={{ cursor: "pointer" }}
        >
          <SoftTypography variant="h6" color="secondary">
            <Icon sx={{ fontWeight: "bold" }}>close</Icon>
          </SoftTypography>
        </SoftBox>
        <SoftBox component={NavLink} to="/" display="flex" alignItems="center">
          {brand && (
            <SoftBox component="img" src={brand} alt="Aprajita Retails Logo" width="2rem" />
          )}
          <SoftBox
            width={!brandName && "100%"}
            sx={(theme) => sidenavLogoLabel(theme, { miniSidenav })}
          >
            <SoftTypography component="h6" variant="button" fontWeight="medium">
              {brandName}
            </SoftTypography>
          </SoftBox>
        </SoftBox>
      </SoftBox>
      <Divider />
      <List>{renderRoutes}</List>
    </SidebarRoot>
  );
}

// Setting default values for the props of Sidenav
Sidebar.defaultProps = {
  color: "info",
  brand: "",
};

// Typechecking props for the Sidenav
Sidebar.propTypes = {
  color: PropTypes.oneOf(["primary", "secondary", "info", "success", "warning", "error", "dark"]),
  brand: PropTypes.string,
  brandName: PropTypes.string.isRequired,
  routes: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default Sidebar;

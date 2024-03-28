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

// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";

// @mui material components
import Collapse from "@mui/material/Collapse";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Icon from "@mui/material/Icon";

import ExpandLess from "@mui/icons-material/ExpandLess";
import ExpandMore from "@mui/icons-material/ExpandMore";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";

// Custom styles for the SidenavCollapse
import {
  collapseItem,
  collapseSubIconBox,
  collapseIcon,
  collapseText,
} from "baseapp/Sidenav/styles/sidenavCollapse";

// Aprajita Retails Dashboard context
import { useSoftUIController } from "context";

function SubSidebarCollapse({ color, icon, name, bgColor,children, active, noCollapse, open, ...rest }) {
  const [controller] = useSoftUIController();
  const { miniSidenav, transparentSidenav } = controller;

  const bgSideNavbar=bgColor?false:transparentSidenav;
  
  return (
    <>
      <ListItem component="li" sx={{ pt: 1 }}>
        <SoftBox {...rest} sx={(theme) => collapseItem(theme, { active, transparentSidenav })}>
          <ListItemIcon
            sx={(theme) => collapseSubIconBox(theme, { active, transparentSidenav, color })}
          >
            {typeof icon === "string" ? (
              <Icon sx={(theme) => collapseIcon(theme, { active })}>{icon}</Icon>
            ) : (
              icon
            )}
          </ListItemIcon>

          <ListItemText
            primary={name}
            sx={(theme) => collapseText(theme, { miniSidenav, transparentSidenav, active })}
          />
          {!noCollapse && (open ? <ExpandLess /> : <ExpandMore />)}
        </SoftBox>
      </ListItem>
      {children && (
        <Collapse in={open} unmountOnExit>
          {children}
        </Collapse>
      )}
    </>
  );
}

// Setting default values for the props of SidebarCollapse
SubSidebarCollapse.defaultProps = {
  color: "info",
  active: false,
  noCollapse: false,
  children: false,
  open: false,
  bgColor: false,
};

// Typechecking props for the SidebarCollapse
SubSidebarCollapse.propTypes = {
  color: PropTypes.oneOf(["primary", "secondary", "info", "success", "warning", "error", "dark"]),
  icon: PropTypes.node.isRequired,
  name: PropTypes.string.isRequired,
  children: PropTypes.node,
  active: PropTypes.bool,
  noCollapse: PropTypes.bool,
  open: PropTypes.bool,
  bgColor: PropTypes.bool,
};

export default SubSidebarCollapse;

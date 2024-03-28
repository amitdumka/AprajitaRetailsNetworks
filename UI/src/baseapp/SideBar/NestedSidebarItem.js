// react-router-dom components
import { useLocation, NavLink } from "react-router-dom";

// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";

// @mui material components
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import Link from "@mui/material/Link";
import Icon from "@mui/material/Icon";
import * as React from "react";
// @mui material components
import Collapse from "@mui/material/Collapse";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ExpandLess from "@mui/icons-material/ExpandLess";
import ExpandMore from "@mui/icons-material/ExpandMore";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import SidebarCollapse from "baseapp/SideBar/SidebarCollapse";
import SubSidebarCollapse from "baseapp/SideBar/SubSidebarCollapse";

// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
import SoftButton from "components/SoftButton";
// Aprajita Retails Dashboard context
import { useSoftUIController } from "context";
// Custom styles for the SidenavCollapse
import {
  collapseItem,
  collapseIconBox,
  collapseIcon,
  collapseText,
} from "baseapp/Sidenav/styles/sidenavCollapse";

function NestedSidebarItem({
  color,
  name,
  children,
  open,
  noCollapse,
  active,
  icon,
  route,
  key,
  collapse,
  collapseName,
  nestedCollapseName,
  ...rest
}) {
  const [open1, setOpen] = React.useState(true);
  const [controller] = useSoftUIController();
  const { miniSidenav, transparentSidenav } = controller;

  const handleExpandClick = () => {
    setOpen(!open1);
  };
  let nestedMenuItem;
  if (!noCollapse) {
    const nestedItem = collapse.map(({ type, name,  title, noCollapse, key, route, href }) => {
      let returnValue;
      if (type === "collapse") {
        let nActive = nestedCollapseName === key ? true : false;
        returnValue = href ? (
          <Link
            href={href}
            key={key}
            target="_blank"
            rel="noreferrer"
            sx={{ textDecoration: "none" }}
          >
            <ListItem component="li">
              <ListItemIcon
                sx={(theme) => collapseIconBox(theme, { nActive, transparentSidenav, color })}
              >
                {typeof icon === "string" ? (
                  <Icon sx={(theme) => collapseIcon(theme, { nActive })}>{icon}</Icon>
                ) : (
                  icon
                )}
              </ListItemIcon>

              <ListItemText
                primary={name}
                sx={(theme) => collapseText(theme, { miniSidenav, transparentSidenav, nActive })}
              />
            </ListItem>
          </Link>
        ) : (
          <NavLink key={key} to={route}>
            <SubSidebarCollapse
              color={color}
              key={key}
              name={name}
              icon={icon}
              active={nActive}
              noCollapse={noCollapse}
              bgColor={true}
            />
            
               
          </NavLink>
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
    });
    nestedMenuItem = nestedItem;
  }

  if (noCollapse) {
    return (
      <NavLink to={route} key={key}>
        <SidebarCollapse
          color={color}
          key={key}
          name={name}
          icon={icon}
          active={active}
          noCollapse={noCollapse}
        />
      </NavLink>
    );
  } else {
    return (
      <NavLink to={route} key={key}>
        <SidebarCollapse
          onClick={handleExpandClick}
          color={color}
          key={key}
          name={name}
          icon={icon}
          active={active}
          noCollapse={noCollapse}
          open={open1}
        >
          <List component="div"  sx={{ pl: 4 }}>
            {nestedMenuItem}
          </List>
        </SidebarCollapse>
      </NavLink>
    );
  }
}

NestedSidebarItem.defaultProps = {
  color: "info",
  active: false,
  noCollapse: false,
  children: false,
  open: false,
};
NestedSidebarItem.propTypes = {
  color: PropTypes.oneOf(["primary", "secondary", "info", "success", "warning", "error", "dark"]),
  icon: PropTypes.node.isRequired,
  name: PropTypes.string.isRequired,
  children: PropTypes.node,
  active: PropTypes.bool,
  noCollapse: PropTypes.bool,
  open: PropTypes.bool,
  route: PropTypes.string.isRequired,
  key: PropTypes.string.isRequired,
  collapse: PropTypes.arrayOf(PropTypes.object),
};
export default NestedSidebarItem;

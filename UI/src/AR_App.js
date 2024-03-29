/**
 * Aprajita Retails App
 *  This is will be the main entry point for the App
 *  It is customized for Aprajita Retails
 *  Author: Amit Kumar
 *  Date: 2024-03-29
 */

import { useState, useEffect, useMemo } from "react";

// react-router components
import { Routes, Route, Navigate, useLocation } from "react-router-dom";

// @mui material components
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Icon from "@mui/material/Icon";

// Aprajita Retails React components
import SoftBox from "components/SoftBox";

// Aprajita Retails React
import Sidebar from "baseapp/SideBar";
import Configurator from "baseapp/Configurator";

// Aprajita Retails React routes
import routes from "./routes";
import { ProtectedRoute } from "./ProtectedRoute";

// Aprajita Retails React themes
import theme from "assets/theme";

//Aprajita Retails UI Section
import ConfigButton from "./UI/componets/controls/configButton";
import { getRoutes } from "./UI/componets/utils/utils";

// Aprajita Retails React contexts
import { useSoftUIController, setMiniSidenav, setOpenConfigurator } from "context";

// Images
import brand from "assets/images/logo-ct.png";
import DashboardNavbar from "baseapp/Navbars/DashboardNavbar";

export default function AR_App() {
  const [controller, dispatch] = useSoftUIController();
  const { pathname } = useLocation();
  const [onMouseEnter, setOnMouseEnter] = useState(false);
  const { miniSidenav, direction, layout, openConfigurator, sidenavColor } = controller;

  // Open sidenav when mouse enter on mini sidenav
  const handleOnMouseEnter = () => {
    if (miniSidenav && !onMouseEnter) {
      setMiniSidenav(dispatch, false);
      setOnMouseEnter(true);
    }
  };

  // Close sidenav when mouse leave mini sidenav
  const handleOnMouseLeave = () => {
    if (onMouseEnter) {
      setMiniSidenav(dispatch, true);
      setOnMouseEnter(false);
    }
  };
  
  // Setting page scroll to 0 when changing the route
  useEffect(() => {
    document.documentElement.scrollTop = 0;
    document.scrollingElement.scrollTop = 0;
  }, [pathname]);
  // Change the openConfigurator state
  const handleConfiguratorOpen = () => setOpenConfigurator(dispatch, !openConfigurator);
  const configsButton = (
    <SoftBox
      display="flex"
      justifyContent="center"
      alignItems="center"
      width="3.5rem"
      height="3.5rem"
      bgColor="white"
      shadow="sm"
      borderRadius="50%"
      position="fixed"
      right="2rem"
      bottom="2rem"
      zIndex={99}
      color="dark"
      sx={{ cursor: "pointer" }}
      onClick={handleConfiguratorOpen}
    >
      <Icon fontSize="default" color="inherit">
        settings
      </Icon>
    </SoftBox>
  );
  return (
    <ThemeProvider theme={theme}>
      {/* This API is deprecated. Consider using color-scheme instead. */}
      <CssBaseline enableColorScheme={true} />
      <>
        <Sidebar
          color={sidenavColor}
          brand={brand}
          brandName="Aprajita Retails"
          routes={routes}
          onMouseEnter={handleOnMouseEnter}
          onMouseLeave={handleOnMouseLeave}
        />
        <Configurator />
        {configsButton}
        {/* <ConfigButton onClick={handleConfiguratorOpen} /> */}
      </>
      <Routes>
        {getRoutes(routes)}
        <Route path="*" element={<Navigate to="/dashboard" />} />
      </Routes>
    </ThemeProvider>
  );
}

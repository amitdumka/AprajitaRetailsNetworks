

import routes from "routes";
import { ProtectedRoute } from 'ProtectedRoute';
// react-router components
import { Routes, Route, Navigate, useLocation } from "react-router-dom";
// Aprajita Retails React components
import SoftBox from "components/SoftBox";
import Icon from "@mui/material/Icon";

const getProtectedRoutes = (allRoutes) =>
allRoutes.map((route) => {
  if (route.collapse) {
    return getProtectedRoutes(route.collapse);
  }

  if (route.route) {
    if (route.protected) {
      return(
        <Route key={route.key} element={<ProtectedRoute />}>
          <Route path={route.route} element={route.component} />
        </Route>
      );
    }
    return <Route path={route.route} element={route.component} key={route.key} />;
  }

  return null;
});


const getRoutes = (allRoutes) =>
allRoutes.map((route) => {
  if (route.collapse) {
    return getRoutes(route.collapse);
  }

  if (route.route) {
    return <Route exact path={route.route} element={route.component} key={route.key} />;
  }

  return null;
});


export { getProtectedRoutes, getRoutes }
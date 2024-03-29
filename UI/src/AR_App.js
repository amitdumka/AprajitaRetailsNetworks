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

// Aprajita Retails React routes
import routes from "./routes";
import { ProtectedRoute } from './ProtectedRoute';

//Aprajita Retails UI Section 
import ConfigButton from "./UI/componets/controls/configButton";


export default function AR_App() {
    const { pathname } = useLocation();



    return (
        <ThemeProvider theme={theme}>
        {/* This API is deprecated. Consider using color-scheme instead. */}
        <CssBaseline enableColorScheme={true}/> 

        </ThemeProvider>
    );

}
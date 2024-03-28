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

/* eslint-disable react/prop-types */
/**
  This file is used for controlling the dark and light state of the TimelineList and TimelineItem.
*/

import { createContext, useContext } from "react";

// The Timeline main context
const Timeline = createContext();

// Timeline context provider
function TimelineProvider({ children, value }) {
  return <Timeline.Provider value={value}>{children}</Timeline.Provider>;
}

// Timeline custom hook for using context
function useTimeline() {
  return useContext(Timeline);
}

export { TimelineProvider, useTimeline };
/* eslint-enable react/prop-types */
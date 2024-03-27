import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "App";
import { AuthProvider } from "./auth-context/auth.context";

// Aprajita Retails React Context Provider
import { SoftUIControllerProvider } from "context";

let user = localStorage.getItem("user");
user = JSON.parse(user);

// ReactDOM.render(
//   <BrowserRouter>
//     <SoftUIControllerProvider>
//       <AuthProvider userData={user}>
//         <App />
//       </AuthProvider>
//     </SoftUIControllerProvider>
//   </BrowserRouter>,
//   document.getElementById("root")
// );

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <BrowserRouter>
    <SoftUIControllerProvider>
      <App />
    </SoftUIControllerProvider>
  </BrowserRouter>
);

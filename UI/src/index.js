import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import AR_App from "AR_App";
import { AuthProvider } from "./auth-context/auth.context";
// Registering Syncfusion license key
import { registerLicense } from "@syncfusion/ej2-base";

 
// Aprajita Retails React Context Provider
import { SoftUIControllerProvider } from "context";

let user = localStorage.getItem("user");
user = JSON.parse(user);
registerLicense("ORg4AjUWIQA/Gnt2UFhhQlJBfV5AQmBIYVp/TGpJfl96cVxMZVVBJAtUQF1hTX5QdE1iW3pZcHJSQ2le");
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
      <AuthProvider userData={user}>
        <AR_App />
      </AuthProvider>
    </SoftUIControllerProvider>
  </BrowserRouter>
);

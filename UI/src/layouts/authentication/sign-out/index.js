/**
=========================================================
* Aprajita Retails React - v2.0.0
=========================================================

* Product Page: https://www.aprajitaretails.in/amitkumar/product/soft-ui-dashboard-material-ui
* Copyright 2021 Amit Kumar (https://www.aprajitaretails.in/amitkumar)

Coded by Amit Kumar (www.aprajitaretails.in/amitkumar)

 =========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/
import { useEffect } from "react";

import AuthApi from "../../../api/auth";
import { useNavigate } from 'react-router-dom';
import { useAuth } from "../../../auth-context/auth.context";

function SignOut() {
  const navigate = useNavigate();
  const { setUser } = useAuth();
  let { user } = useAuth();

  const handleLogout = async () => {
    await AuthApi.Logout(user);
    await setUser(null);
    localStorage.removeItem("user");
    return navigate("/authentication/sign-in");
  };

  useEffect(() => {
    handleLogout();
  }, []);

  return null;
}

export default SignOut;

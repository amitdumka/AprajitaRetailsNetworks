// @mui material components
//import Grid from "@mui/material/Grid";
//import Card from "@mui/material/Card";
// Aprajita Retails Dashboard components
//import SoftBox from "components/SoftBox";
//import SoftTypography from "components/SoftTypography";

// Aprajita Retails Dashboard baseapp
import DashboardLayout from "baseapp/LayoutContainers/DashboardLayout";
//import PageLayout from "baseapp/LayoutContainers/PageLayout";
import Footer from "baseapp/Footer";
//import DashboardNavbar from "baseapp/Navbars/DashboardNavbar";
//import SoftButton from "components/SoftButton";


function BasePage() {
  return (
    <DashboardLayout>
      <h1>Base Page</h1>
      <Footer />
    </DashboardLayout>
  );
}

export default BasePage;

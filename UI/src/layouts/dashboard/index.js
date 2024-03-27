// @mui material components
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// Aprajita Retails React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Aprajita Retails React examples
import DashboardLayout from "baseapp/LayoutContainers/DashboardLayout";
import DashboardNavbar from "baseapp/Navbars/DashboardNavbar";
import Footer from "baseapp/Footer";



// Dashboard layout components
import BuildByDevelopers from "layouts/dashboard/components/BuildByDevelopers";
import WorkWithTheRockets from "layouts/dashboard/components/WorkWithTheRockets";
import VouchersInfo from "layouts/dashboard/components/Projects";
import InvoiceOverview from "layouts/dashboard/components/OrderOverview";
import SalesInfo from "layouts/dashboard/components/SalesInfo";
// Aprajita Retails React base styles
import typography from "assets/theme/base/typography";

// Data


function Dashboard() {
  const { size } = typography;
   

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox py={3}>
       <SalesInfo/>
        <SoftBox mb={3}>
          <Grid container spacing={3}>
            <Grid item xs={12} lg={7}>
              <BuildByDevelopers />
            </Grid>
            <Grid item xs={12} lg={5}>
              <WorkWithTheRockets />
            </Grid>
          </Grid>
        </SoftBox>
        
        <Grid container spacing={3}>
          <Grid item xs={12} md={6} lg={8}>
            <VouchersInfo />
          </Grid>
          <Grid item xs={12} md={6} lg={4}>
            <InvoiceOverview />
          </Grid>
        </Grid>
      </SoftBox>
      <Footer />
    </DashboardLayout>
  );
}
export default Dashboard;

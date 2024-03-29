// @mui material components
import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Aprajita Retails Dashboard baseapp
import DashboardLayout from "baseapp/LayoutContainers/DashboardLayout";
import Footer from "baseapp/Footer";
import DashboardNavbar from "baseapp/Navbars/DashboardNavbar";
import SoftButton from "components/SoftButton";

import MTables from "apps/base/tables/MTables";
import SFTables from "apps/base/tables/SFTables";

import TableHeader from "apps/base/tables/tableHeader";

// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";
function ListPage(props, ...rest) {
  let TableUI;
  let UIName = "SF";
  
  if (UIName === "SF") {
    TableUI = (
      <>
        <SFTables dataSource={props.dataSource} settings={props.settings}  />
      </>
    );
  } else {
    TableUI = (
      <>
        <MTables dataSource={props.dataSource} />
      </>
    );
  }

  return (
    <DashboardLayout>
       
      <TableHeader title={props.settings.title} icon={props.settings.icon}  subTitle="Apajita Retails, MBO, Dumka"/>
      <SoftBox mt={5} mb={1} borderRadius="lg" bgColor="transparent">
        <Grid container spacing={2}>
          
          <Grid item>
            <SoftBox
              mt={-6}
              mb={3}
              variant="gradient"
              bgColor="transparent"
              borderRadius="xl"
              shadow="xl"
            >
              {TableUI}
            </SoftBox>
          </Grid>
        </Grid>
      </SoftBox>
      <Footer />
    </DashboardLayout>
  );
}

ListPage.propTypes = {
  dataSource: PropTypes.array.isRequired,
  title: PropTypes.string.isRequired,
};

export default ListPage;

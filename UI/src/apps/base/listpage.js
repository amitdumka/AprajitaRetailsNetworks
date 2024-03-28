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
// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";
function ListPage(props, ...rest) {
  // const rows: GridRowsProp = [
  //     { id: 1, col1: 'Hello', col2: 'World' },
  //     { id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
  //     { id: 3, col1: 'MUI', col2: 'is Amazing' },
  //   ];
  //   const columns: GridColDef[] = [
  //     { field: 'col1', headerName: 'Column 1', width: 150 },
  //     { field: 'col2', headerName: 'Column 2', width: 150 },
  //   ];

  let TableUI;
  if (props.UIName === "SF") {
    TableUI = (
      <>
        <SFTables tableData={props.tableData} />
      </>
    );
  } else {
    TableUI = (
      <>
        <MTables tableData={props.tableData} />
      </>
    );
  }

  return (
    <DashboardLayout>
      <DashboardNavbar />
      <SoftBox mt={2} mb={1} borderRadius="lg" bgColor="transparent">
        <Grid container spacing={2}>
          <Grid item  alignSelf={"flex-end"}  >
            <SoftBox display="flex" alignItems="end" mb={-5} borderRadius="lg" bgColor="white" shadow="lg" p={2} >
              <SoftTypography color="dark" textGradient={true} variant="h4" fontWeight="medium" textTransform="capitalize">Employees</SoftTypography>
            </SoftBox>
          </Grid>
          <Grid item>
            <SoftBox
              mt={5}
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
  title: PropTypes.string.isRequired,
  route: PropTypes.string,
  apiurl: PropTypes.string,
  baseurl: PropTypes.string.isRequired,
  className: PropTypes.string.isRequired,
  UIName: PropTypes.string.isRequired,
  tableData: PropTypes.array.isRequired,
};

export default ListPage;

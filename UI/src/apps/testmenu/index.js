import { List } from "@mui/material";
import ListPage from "apps/base/listpage";
import employees from "apps/base/mockdata/mockTable";
import Shop from "baseapp/Icons/Shop";
import Office from "baseapp/Icons/Office";
import Settings from "baseapp/Icons/Settings";

function TestPage() {
  const employee_settings = {
    title: "Employees",
    className: "Employee",
    baseurl: "/testmenu",
    apiurl: "/api/testmenu",
    route: "/testmenu",
    UIName: "SF",
    paging: true,
    pageSize: 10,
    sorting: true,
    filters: true,
    pk: "id",
    fk: false,
    showStore: false,
    icon: <Office size="12px" />,
  };

  return (
    <>
      <ListPage dataSource={employees} settings={employee_settings} title="Employees" />
    </>
  );
}

export default TestPage;


import { List } from "@mui/material";
import ListPage from "apps/base/listpage";
import employees from "apps/base/mockdata/mockTable";



function TestPage(){
    return(
        <>
            <ListPage UIName="SF" tableData={employees} title="Test Menu" baseurl="/testmenu" apiurl="/api/testmenu" route="/testmenu" className="employees" />
        </>
    );
}


export default TestPage
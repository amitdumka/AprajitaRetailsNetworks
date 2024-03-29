import {
  GridComponent,
  ColumnsDirective,
  ColumnDirective,
  Inject,
  Filter,
  Reorder,
  IFilter,
  ColumnChooser,
  ColumnMenu,
  VirtualScroll,
  Sort,
  PdfExport,
  Page,
  Resize,
  ForeignKey,
  Toolbar,
} from "@syncfusion/ej2-react-grids";
import SoftButton from "components/SoftButton";
import { Edit, ExcelExport } from "@syncfusion/ej2-react-grids";
import { DropDownListComponent } from "@syncfusion/ej2-react-dropdowns";
import { DataManager, Query, UrlAdaptor } from "@syncfusion/ej2-data";
import { ClickEventArgs } from "@syncfusion/ej2-navigations";
import { ddlData, toolbarOptions } from "./SFHelper";
//import "./grid-overview.css";
import "App.css";
// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";

function SFTables(props) {
  const fields = { text: "text", value: "value" };
  //Declared Variables
  let ddObj;
  let gridInstance;
  const { dataSource, settings } = props;
  return (
    <>
      <SoftBox
        mt={5}
        mb={1}
        ml={2}
        pt={1}
        bgColor="transparent"
        shodow="md"
        variant="gradient"
        borderRadius="lg"
      >
        <div style={{ paddingBottom: "18px" }} mr={5}>
          <DropDownListComponent
            id="games"
            width="100"
            dataSource={ddlData}
            index={0}
            ref={(dropdownlist) => {
              ddObj = dropdownlist;
            }}
            fields={fields}
            //change={onChange.bind(this)}
            placeholder="Select a Data Range"
            popupHeight="240px"
          />

          <SoftButton
            style={{ marginLeft: "20px", marginRight: "20px" }}
            color="primary"
            size="small"
            circular={true}
            variant="gradient"
          >
            Add
          </SoftButton>

          <span id="msg"></span>
          <br />
        </div>
      </SoftBox>
      <SoftBox pb={2} bgColor="transparent" pl={1} pr={1}>
        <GridComponent
          mb={5}
          pb={10}
          id="DefaultExport"
          enableHeaderFocus={true}
          enableHover={false}
          enableVirtualization={true}
          allowPaging={true}
          dataSource={dataSource}
          toolbar={toolbarOptions}
          rowHeight={38}
          autoFit={true}
          height="400"
          allowSorting={true}
          allowExcelExport={true}
          allowPdfExport={true}
          showColumnChooser={true}
          allowResizing={true}
          allowReordering={true}
          gridLines="Default"
          showColumnMenu={true}
          allowFiltering={true}
          allowSelection={true}
          ref={(g) => {
            gridInstance = g;
          }}
        >
          <Inject
            services={[
              Toolbar,
              ColumnMenu,
              ColumnChooser,
              Resize,
              VirtualScroll,
              Sort,
              Page,
              ExcelExport,
              Edit,
              PdfExport,
              Filter,
              ForeignKey,
              Reorder,
            ]}
          />
        </GridComponent>
      </SoftBox>
    </>
  );
}

SFTables.propTypes = {
  dataSource: PropTypes.array.isRequired,
};

export default SFTables;

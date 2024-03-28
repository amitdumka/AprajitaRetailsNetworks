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
import { RatingComponent } from "@syncfusion/ej2-react-inputs";
import { DataManager, Query, UrlAdaptor } from "@syncfusion/ej2-data";
import { ClickEventArgs } from "@syncfusion/ej2-navigations";
// prop-types is a library for typechecking of props.
import PropTypes from "prop-types";
//import "./grid-overview.css";
import "App.css";
// Aprajita Retails Dashboard components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

function SFTables(props) {
  const entities = props.tableData;

  let dReady = false;
  let dtTime = false;
  let isDataBound = false;
  let isDataChanged = true;
  let intervalFun;
  let clrIntervalFun;
  let clrIntervalFun1;
  let clrIntervalFun2;
  let dropSlectedIndex = null;
  let ddObj;
  let gridInstance;
  let stTime;
  const ddlData = [
    { text: "5 Rows", value: "5" },
    { text: "10 Rows", value: "10" },
    { text: "100 Rows", value: "100" },
    { text: "500 Rows", value: "500" },
  ];
  const fields = { text: "text", value: "value" };
  function onDataBound() {
    clearTimeout(clrIntervalFun);
    clearInterval(intervalFun);
    dtTime = true;
  }
  const FilterOptions = {
    type: "Excel",
  };
  function emptyMessageTemplate() {
    return (
      <div className="emptyRecordTemplate">
        <img
          src="src/grid/images/emptyRecordTemplate.svg"
          className="e-emptyRecord"
          alt="No record"
        />
        <span>There is no data available to display at the moment.</span>
      </div>
    );
  }
  const template = emptyMessageTemplate;
  const toolbarOptions = [
    "Add",
    "Edit",
    "Delete",
    "Update",
    "Cancel",
    "Print",
    "Search",
    "ColumnChooser",
    "ExcelExport",
    "PdfExport",
  ];
  function onLoad(args) {
    document.getElementById("DefaultExport").ej2_instances[0].on("data-ready", () => {
      dReady = true;
      stTime = performance.now();
    });
    var observer = new MutationObserver((mutations) => {
      mutations.forEach(() => {
        if (dReady && stTime && isDataChanged) {
          let msgEle = document.getElementById("msg");
          let val = (performance.now() - stTime).toFixed(0);
          stTime = null;
          dReady = false;
          dtTime = false;
          isDataChanged = false;
          msgEle.innerHTML = "Load Time: " + "<b>" + val + "</b>" + "<b>ms</b>";
          msgEle.classList.remove("e-hide");
        }
      });
    });
    observer.observe(document.getElementById("overviewgrid"), {
      attributes: true,
      childList: true,
      subtree: true,
    });
  }
  function onChange() {
    ddObj.hidePopup();
    dropSlectedIndex = null;
    let index = ddObj.value;
    clearTimeout(clrIntervalFun2);
    clrIntervalFun2 = setTimeout(() => {
      isDataChanged = true;
      stTime = null;
      let contentElement = gridInstance.contentModule.getPanel().firstChild;
      contentElement.scrollLeft = 0;
      contentElement.scrollTop = 0;
      gridInstance.pageSettings.currentPage = 1;
      stTime = performance.now();
      if (gridInstance.query.params.length > 1) {
        for (let i = 0; i < gridInstance.query.params.length; i++) {
          if (gridInstance.query.params[i].key === "dataCount") {
            gridInstance.query.params[i].value = index.toString();
            break;
          }
        }
      } else {
        gridInstance.query.params[0].value = index.toString();
      }
      gridInstance.setProperties({ dataSource: data });
    }, 100);
  }
  function toolbarClick(args) {
    switch (args.item.id) {
      case "DefaultExport_pdfexport":
        gridInstance.pdfExport();
        break;
      case "DefaultExport_excelexport":
        gridInstance.excelExport();
        break;
      case "DefaultExport_csvexport":
        gridInstance.csvExport();
        break;
    }
  }
  const editSettings = { allowEditing: true, allowAdding: true, allowDeleting: true };
  const orderidRules = { required: true, number: true };
  const editparams = {
    params: {
      dataSource: new DataManager(entities),
      fields: { text: "ShipCountry", value: "ShipCountry" },
    },
  };
  const validationRule = { required: true };
  const pageSettings = { pageSize: 5 };
  const format = { type: "dateTime", format: "M/d/y hh:mm a" };

  return (
    <>
      <SoftBox mt={5} mb={1} ml={2} pt={1} bgColor="transparent" shodow="md" variant="gradient" borderRadius="lg">
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
            change={onChange.bind(this)}
            placeholder="Select a Data Range"
            popupHeight="240px"
          />
          
          <SoftButton style={{ marginLeft: "20px" ,marginRight: "20px" }} color="primary" size="small" circular={true} variant="gradient" >
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
          allowPaging={true}
          pageSettings={pageSettings}
          height="450"
          allowSorting={true}
          id="DefaultExport"
          allowExcelExport={true}
          allowPdfExport={true}
          showColumnChooser={true}
          allowResizing={true}
          dataSource={entities}
          toolbarClick={toolbarClick.bind(this)}
          loadingIndicator={{ indicatorType: "Shimmer" }}
          allowReordering={true}
          editSettings={editSettings}
          enableHover={false}
          enableVirtualization={true}
          rowHeight={38}
          autoFit={true}
          gridLines="Default"
          showColumnMenu={true}
          allowFiltering={true}
          allowSelection={true}
          toolbar={toolbarOptions}
          enableHeaderFocus={true}
          ref={(g) => {
            gridInstance = g;
          }}
          emptyRecordTemplate={template.bind(this)}
          //query={query}
          // actionComplete={onComplete.bind(this)}
          // load={onLoad.bind(this)}
          dataBound={onDataBound.bind(this)}
          //filterSettings={gridFilter}
          //selectionSettings={select}
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

export default SFTables;

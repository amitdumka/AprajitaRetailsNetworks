// let dReady = false;
//   let dtTime = false;
//   let isDataBound = false;
//   let isDataChanged = true;
//   let intervalFun;
//   let clrIntervalFun;
//   let clrIntervalFun1;
//   let clrIntervalFun2;
//   let dropSlectedIndex = null;
  
//   let gridInstance;
//   let stTime;

//   function onDataBound() {
//     clearTimeout(clrIntervalFun);
//     clearInterval(intervalFun);
//     dtTime = true;
//   }
//   const FilterOptions = {
//     type: "Excel",
//   };
//   function emptyMessageTemplate() {
//     return (
//       <div className="emptyRecordTemplate">
//         <img
//           src="src/grid/images/emptyRecordTemplate.svg"
//           className="e-emptyRecord"
//           alt="No record"
//         />
//         <span>No record available.</span>
//       </div>
//     );
//   }
//   const template = emptyMessageTemplate;
//   const toolbarOptions = [
//     "Add",
//     "Edit",
//     "Delete",
//     "Update",
//     "Cancel",
//     "Print",
//     "Search",
//     "ColumnChooser",
//     "ExcelExport",
//     "PdfExport",
//   ];
//   function onLoad(args) {
//     document.getElementById("DefaultExport").ej2_instances[0].on("data-ready", () => {
//       dReady = true;
//       stTime = performance.now();
//     });
//     var observer = new MutationObserver((mutations) => {
//       mutations.forEach(() => {
//         if (dReady && stTime && isDataChanged) {
//           let msgEle = document.getElementById("msg");
//           let val = (performance.now() - stTime).toFixed(0);
//           stTime = null;
//           dReady = false;
//           dtTime = false;
//           isDataChanged = false;
//           msgEle.innerHTML = "Load Time: " + "<b>" + val + "</b>" + "<b>ms</b>";
//           msgEle.classList.remove("e-hide");
//         }
//       });
//     });
//     observer.observe(document.getElementById("overviewgrid"), {
//       attributes: true,
//       childList: true,
//       subtree: true,
//     });
//   }
//   function onChange() {
//     ddObj.hidePopup();
//     dropSlectedIndex = null;
//     let index = ddObj.value;
//     clearTimeout(clrIntervalFun2);
//     clrIntervalFun2 = setTimeout(() => {
//       isDataChanged = true;
//       stTime = null;
//       let contentElement = gridInstance.contentModule.getPanel().firstChild;
//       contentElement.scrollLeft = 0;
//       contentElement.scrollTop = 0;
//       gridInstance.pageSettings.currentPage = 1;
//       stTime = performance.now();
//       if (gridInstance.query.params.length > 1) {
//         for (let i = 0; i < gridInstance.query.params.length; i++) {
//           if (gridInstance.query.params[i].key === "dataCount") {
//             gridInstance.query.params[i].value = index.toString();
//             break;
//           }
//         }
//       } else {
//         gridInstance.query.params[0].value = index.toString();
//       }
//       gridInstance.setProperties({ dataSource: data });
//     }, 100);
//   }
//   function toolbarClick(args) {
//     switch (args.item.id) {
//       case "DefaultExport_pdfexport":
//         gridInstance.pdfExport();
//         break;
//       case "DefaultExport_excelexport":
//         gridInstance.excelExport();
//         break;
//       case "DefaultExport_csvexport":
//         gridInstance.csvExport();
//         break;
//     }
//   }
//   const editSettings = { allowEditing: true, allowAdding: true, allowDeleting: true };
//   const orderidRules = { required: true, number: true };
//   const editparams = {
//     params: {
//       dataSource: new DataManager(datasource),
//       fields: { text: "ShipCountry", value: "ShipCountry" },
//     },
//   };
//   const validationRule = { required: true };
//   const pageSettings = { pageSize: 5 };
//   const format = { type: "dateTime", format: "M/d/y hh:mm a" };




//   //pageSettings={pageSettings}
  
//   
//   //toolbarClick={toolbarClick.bind(this)}
//   //loadingIndicator={{ indicatorType: "Shimmer" }}
//   //
//   //editSettings={editSettings}
  
//   //toolbar={toolbarOptions}
//   //
  
//   //emptyRecordTemplate={template.bind(this)}
//   //query={query}
//   // actionComplete={onComplete.bind(this)}
//   // load={onLoad.bind(this)}
//   //dataBound={onDataBound.bind(this)}
//   //filterSettings={gridFilter}
//   //selectionSettings={select}
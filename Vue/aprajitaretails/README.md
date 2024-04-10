#Things to Do 

#Team Section 
  There should be a list which will show all location or make it static
 
#Header and title of app need to set once and will be used in all pages using variable or state


# days.js  check for use
# Nuxt Calendly check for use and implement
# Vcandler same as above
# Nuxt Modules check for use and implement
 Link https://nuxt.com/modules

# SupaBase  For Auth 

# Fonts 
 Many Fonts option available , use as desroed as possible
# SnackBar is added
  Check for uses and how to use

 #DataGrid 
 vue3-datagrid
 syncfusion datagrid 


 #Syncfusion datagrid
  need to import 
  "dependencies": { 

    "@syncfusion/ej2-vue-grids": "*", 

    ---

    "vue-class-component": "^8.0.0-rc.1" 

  }, 
  npm i --legacy-peer-deps // use this if npm version is higher than 7
  code below:
  
  import {
  ColumnChooser,
  ColumnDirective,
  ColumnsDirective,
  CommandColumn,
  ContextMenu,
  Edit,
  ExcelExport,
  Filter,
  ForeignKey,
  Freeze,
  Grid,
  GridComponent,
  Group,
  Page,
  PdfExport,
  Reorder,
  Resize,
  RowDD,
  Search,
  Selection,
  Sort,
  Toolbar,
} from '@syncfusion/ej2-vue-grids'

Grid.Inject(CommandColumn)
Grid.Inject(ColumnChooser)
Grid.Inject(ContextMenu)
Grid.Inject(Edit)
Grid.Inject(ExcelExport)
Grid.Inject(Filter)
Grid.Inject(ForeignKey)
Grid.Inject(Freeze)
Grid.Inject(Group)
Grid.Inject(Page)
Grid.Inject(PdfExport)
Grid.Inject(Reorder)
Grid.Inject(Resize)
Grid.Inject(RowDD)
Grid.Inject(Search)
Grid.Inject(Selection)
Grid.Inject(Sort)
Grid.Inject(Toolbar)

export default {
  data() {
    return {}
  },
  components: {
    'ejs-grid': GridComponent,
    'e-columns': ColumnsDirective,
    'e-column': ColumnDirective,
  },
}


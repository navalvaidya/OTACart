package com.revnomix;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.FormulaEvaluator;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class Utility {
	@SuppressWarnings("deprecation")
	public String fetchUrl(String hotel,String path)throws IOException{
		//String path = this.getServletContext().getRealPath("/WEB-INF/DataFiles/url2.xlsx");
		System.out.println(path);
		StringBuffer buffer = new StringBuffer();
		FileInputStream fis = new FileInputStream(new File(path));
	 	XSSFWorkbook wb = new XSSFWorkbook(fis);
	 	XSSFSheet sheet = wb.getSheetAt(0);
	 	FormulaEvaluator formulaEvaluator = wb.getCreationHelper().createFormulaEvaluator();
	 	
		boolean flag= false ; 
	 	 for(Row row : sheet){
				for (Cell cell : row){
					if(row.getRowNum() > 0 ){
						if(flag==true){
							buffer.append(cell.getStringCellValue());
						}
						switch(formulaEvaluator.evaluateInCell(cell).getCellType()){
							case Cell.CELL_TYPE_STRING:
								if(!(cell.getStringCellValue().equalsIgnoreCase("None"))){
									if(cell.getStringCellValue().equalsIgnoreCase(hotel)){
										//System.out.print("Showing URL for "+cell.getStringCellValue()+ "\n");
										flag=true;
									}
								}
								break;
	
							case Cell.CELL_TYPE_NUMERIC:
							break;
						}
					}
				}
				flag=false;
			}
			wb.close();
			
	     String url= buffer.toString();
	     return url; 
	}
	
	@SuppressWarnings("deprecation")
	public String readReview(String excelFilePath){
		FileInputStream inputStream;
		StringBuffer buffer = new StringBuffer();
		try {
			inputStream = new FileInputStream(new File(excelFilePath));
			Workbook workbook = new XSSFWorkbook(inputStream);
	        Sheet firstSheet = workbook.getSheetAt(0);
	        Iterator<Row> iterator = firstSheet.iterator();
	        
	        while (iterator.hasNext()) {
	            Row nextRow = iterator.next();
	            Iterator<Cell> cellIterator = nextRow.cellIterator();
	             
	            while (cellIterator.hasNext()) {
	                Cell cell = cellIterator.next();
	                 
	                switch (cell.getCellType()) {
	                    case Cell.CELL_TYPE_STRING:
	                        
	                        if(cell.getStringCellValue()!=null){
	                        	System.out.print(cell.getStringCellValue());
	                        	buffer.append(cell.getStringCellValue()+"[split]");
	                        }
	                        break;
	                }
	            }
	            System.out.println();
	        }
	         
	        workbook.close();
	        inputStream.close();
		}catch (Exception e) {
			e.printStackTrace();
		}
		return buffer.toString();
	}

}


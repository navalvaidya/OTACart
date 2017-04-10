package com.revnomix;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.DecimalFormatSymbols;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.FormulaEvaluator;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.xssf.usermodel.XSSFSheet;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

/**
 * Servlet implementation class Perhoteldata
 */
@WebServlet("/Perhoteldata")
public class Perhoteldata extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Perhoteldata() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//System.out.println("Submitting form");
		String hotelname = request.getParameter("hotelname");
		//System.out.println("get : "+hotelname);
		Utility utility = new Utility();
		String context = this.getServletContext().getRealPath("/WEB-INF/DataFiles/url2.xlsx");
		String url = utility.fetchUrl(hotelname,context);
		System.out.println(url);
		String scriptPath = this.getServletContext().getRealPath("/WEB-INF/DataFiles/perhotel2.py");
		String excelPath = this.getServletContext().getRealPath("/WEB-INF/DataFiles");
		System.out.println(excelPath);
		String cmd = "python "+scriptPath+" "+url+" "+excelPath;
		System.out.println(cmd);
		try{
		     Runtime rt = Runtime.getRuntime();
	           Process pr = rt.exec(cmd);
	            
	           // retrieve output from python script
	           BufferedReader bfr = new BufferedReader(new InputStreamReader(pr.getInputStream()));
	           String line = "";
	           while((line = bfr.readLine()) != null) {
	           // display each output line form python script
	           System.out.println("Python output"+line);
	           }
		}catch(Exception e){
			e.printStackTrace();
		}
		
		String filename[] = new String[40];
        String report[] = new String[40];
          
        Float parr[];
        // assigning filename
        for(int i=0 ; i<30 ; i++){
        	filename[i] = new String();
          	filename[i]=i+".xlsx";	
        }
        
        ArrayList<String> perdate = new ArrayList<String>();
        for(int i =0 ;i<30 ;i++){
    		List<Float> pricearr = new ArrayList<Float>();
    		ArrayList<Float> duplicates = new ArrayList<Float>();
    		Boolean dupFound = false;
    		report[i]= new String();
    		String path = this.getServletContext().getRealPath("/WEB-INF/DataFiles/"+filename[i]);
    		report[i] = search(path);
    		StringBuffer s = new StringBuffer();
    		String[] r= report[i].split("\\s+");
    		String[] r1= report[i].split("\\s+");

    		for(int j=0 ; j<r.length ; j++){
    			if(isInteger(r[j])==true){
    				float a = Float.parseFloat(r[j]);
    				//System.out.println("\nINTEGER "+a);
    				pricearr.add(a);
    			}   			
    		}
    		
    		//System.out.println("\n\nOUTPUT "+ s+"\n");
    		//System.out.println("DULICATE ARRAY VALUES ");

    		parr = pricearr.toArray(new Float[pricearr.size()]);
	
    		for (int k = 0; k < parr.length; k++) { 
    			for (int z = k + 1 ; z < parr.length; z++) { 
    				if (parr[k].equals(parr[z]) ){ 
    					//System.out.println(parr[z]+" ");
    					duplicates.add(parr[z]);
    					dupFound = true;
   					} 
   				} 
    		}
    		if(dupFound.equals(false)){
    			float no = 0;
    			duplicates.add(no);
    		}
    		//////////////////duplicte found                		
    		for(int j=0 ; j<r1.length ; j++){
    			if(isInteger(r1[j])==true){
    				float a = Float.parseFloat(r1[j]);
    				if(a== duplicates.get(0)){
	    				 s.append(r1[j]);
	    				 s.append("(S)");
	    				 s.append(" \n");
    				}
    				else{
    					 s.append(r1[j]);
    					 s.append("(N)");
        				 s.append(" \n");
    				}
    			}
    			else{
    				s.append(r[j]);
    				s.append(" ");
    			}    			
    		}
    		//System.out.println("ARRAY");	

    		for(int l=0 ;l< pricearr.size(); l++){
    			//System.out.println("\t"+parr[l]);
    		}
    		
    		String ss = s.toString();
    		perdate.add(i, ss);
    	}
        response.getWriter().print(perdate);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}
	
	@SuppressWarnings("deprecation")
	public String search(String filename)throws IOException{
		
		StringBuffer buffer = new StringBuffer();
		FileInputStream fis = new FileInputStream(new File(filename));
	 	XSSFWorkbook wb = new XSSFWorkbook(fis);
	 	XSSFSheet sheet = wb.getSheetAt(0);
	 	FormulaEvaluator formulaEvaluator = wb.getCreationHelper().createFormulaEvaluator();
	 	
		boolean flag= false ;
	 	 for(Row row : sheet){	
				for (Cell cell : row){
					if(row.getRowNum() > 0 ){
						switch(formulaEvaluator.evaluateInCell(cell).getCellType()){
						case Cell.CELL_TYPE_STRING:
							if(!(cell.getStringCellValue().equalsIgnoreCase("None"))){	
								buffer.append(cell.getStringCellValue()+" ");
								//System.out.print("Showing Disparity for "+cell.getStringCellValue()+ "\n");
								flag=true;
							}
							break;
						case Cell.CELL_TYPE_NUMERIC:
							if(flag==true){
								//System.out.print(cell.getNumericCellValue() + "\t\t");
								buffer.append(cell.getNumericCellValue() + "\n");
							}
							break;
						}
					}
				}
				flag=false;
			}
			
			if(buffer.length() == 0 ){
				buffer.append("No data found");
				//System.out.println("No Disparity for this hotel");
			}
			wb.close();
			
	     String report= buffer.toString();
	     return report;   
	}
	
	

	
	public static boolean isInteger(String str) {
		DecimalFormatSymbols currentLocaleSymbols = DecimalFormatSymbols.getInstance();
	    char localeMinusSign = currentLocaleSymbols.getMinusSign();

	    if ( !Character.isDigit( str.charAt( 0 ) ) && str.charAt( 0 ) != localeMinusSign ) return false;

	    boolean isDecimalSeparatorFound = false;
	    char localeDecimalSeparator = currentLocaleSymbols.getDecimalSeparator();

	    for ( char c : str.substring( 1 ).toCharArray() ){
	        if ( !Character.isDigit( c ) ){
	            if ( c == localeDecimalSeparator && !isDecimalSeparatorFound ){
	                isDecimalSeparatorFound = true;
	                continue;
	            }
	            return false;
	        }
	    }
	    return true;
		}
}

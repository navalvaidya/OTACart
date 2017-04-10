package com.revnomix;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class ProcessReview
 */
@WebServlet("/ProcessReview")
public class ProcessReview extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ProcessReview() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		Utility utility = new Utility();
		String hotelname = request.getParameter("reviewSearch");
		System.out.println(hotelname);
		String context = this.getServletContext().getRealPath("/WEB-INF/DataFiles/url2.xlsx");
		String url = utility.fetchUrl(hotelname,context);
		String reviewScript = this.getServletContext().getRealPath("/WEB-INF/DataFiles/review_parser.py");
		
		String storage = this.getServletContext().getRealPath("/WEB-INF/DataFiles");
		String cmd = "python "+reviewScript+" "+url+" "+storage+"/review_data.csv";
		
		String sentimentScript = this.getServletContext().getRealPath("/WEB-INF/DataFiles/senti_analysis.py");
		String inputPath = this.getServletContext().getRealPath("/WEB-INF/DataFiles/review_data.csv");
		String sentimentOutput = this.getServletContext().getRealPath("/WEB-INF/DataFiles/senti_data.csv");
		String cmd1 = "python "+sentimentScript+" "+storage+" "+sentimentOutput;
		System.out.println(cmd);
		try{
		       Runtime rt = Runtime.getRuntime();
	           Process pr = rt.exec(cmd);
	           System.out.println("executing command");
	           // retrieve output from python script
	           BufferedReader bfr = new BufferedReader(new InputStreamReader(pr.getInputStream()));
	           String line = "";
	           while((line = bfr.readLine()) != null) {
	           // display each output line form python script
	           System.out.println("Python output : "+line);
	           }
	         
	           Runtime rt1 = Runtime.getRuntime();
	           Process pr1 = rt1.exec(cmd1);
	           System.out.println("executing command 1");
	           BufferedReader bfr1 = new BufferedReader(new InputStreamReader(pr1.getInputStream()));
	           String line1 = "";
	           while((line1 = bfr1.readLine()) != null) {
	           // display each output line form python script
	           System.out.println("Python output : "+line1);
	           }
		}catch(Exception e){
			e.printStackTrace();
		}
		StringBuilder strBuild = new StringBuilder();
		System.out.println("Encoding data");
		try {
			String line = "";
			BufferedReader br = new BufferedReader(new FileReader(sentimentOutput));
			ArrayList<String> sentiData = new ArrayList<String>();
			while((line=br.readLine())!=null){
				sentiData.add(line);
			}
			strBuild.append(sentiData+"(split)");
			strBuild.append(hotelname+",,");
			br.close();
			String line1 = "";
			BufferedReader br1 = new BufferedReader(new FileReader(inputPath));
			while((line1=br1.readLine())!=null){
				strBuild.append(line1+",,");
				
			}
			System.out.println("strBuild : "+strBuild);
			br1.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		response.getWriter().print(strBuild.toString());

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}

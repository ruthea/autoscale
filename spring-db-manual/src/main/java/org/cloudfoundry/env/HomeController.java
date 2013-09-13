package org.cloudfoundry.env;

import java.io.IOException;
import java.io.PrintWriter;
import java.text.DateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.Map;

import javax.servlet.http.HttpServletResponse;
import javax.sql.DataSource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.test.jdbc.JdbcTestUtils;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 * Handles requests for the application home page.
 */
@Controller
public class HomeController {
	
	private static final Logger logger = LoggerFactory.getLogger(HomeController.class);
	
	@Autowired private DataSource dataSource;
	
	/**
	 * Simply selects the home view to render by returning its name.
	 */
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String home(Locale locale, Model model) {
		logger.info("Welcome home! the client locale is "+ locale.toString());
		
		Date date = new Date();
		DateFormat dateFormat = DateFormat.getDateTimeInstance(DateFormat.LONG, DateFormat.LONG, locale);
		
		String formattedDate = dateFormat.format(date);
		
		model.addAttribute("serverTime", formattedDate );
		
		return "home";
	}

	@RequestMapping("/env")
	public void env(HttpServletResponse response) throws IOException {
	    response.setContentType("text/plain");
	    PrintWriter out = response.getWriter();
	    out.println("System Environment:");
	    for (Map.Entry<String, String> envvar : System.getenv().entrySet()) {
	        out.println(envvar.getKey() + ": " + envvar.getValue());
	    }
	}

	@RequestMapping(value = "/db-test", method = RequestMethod.GET)
	public String dbTest(Locale locale, Model model) {

	    model.addAttribute("dataSourcePresent", dataSource != null);
	    
	    if(dataSource != null) {
		    JdbcTemplate jt = new JdbcTemplate(dataSource);
		    	int rowCount = JdbcTestUtils.countRowsInTable(jt,  "thing");
		    	model.addAttribute("thingRowCount", rowCount);
	    }
	    else {
		    	model.addAttribute("thingRowCount", "dunno");	    	
	    }
	    	return "db-test";
	}
}

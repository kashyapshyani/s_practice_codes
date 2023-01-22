// import java.util.LinkedList;
// import java.util.Iterator;

// class Try {
//   public static void main(String[] args){
//     LinkedList<String> ll = new LinkedList<>();
//     ll.add("a1");
//     ll.add("a2");
//     System.out.println("Linkedlist="+ll);
//     ll.add("a3");
//     System.out.println("Linkedlist="+ll+"\nnew\n");
//     Iterator<String> it = ll.iterator();
//     while(it.hasNext()){
//       System.out.println(it.next()+"\n");
//     }
//     System.out.println("new\n");
//     // for(String it1: ll){
        
//     // }
//   }
// }


import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
//comment the above line and uncomment below line to use Chrome
//import org.openqa.selenium.chrome.ChromeDriver;
public class PG1 {


    public static void main(String[] args) {
        // declaration and instantiation of objects/variables
    	System.setProperty("webdriver.gecko.driver","C:\\geckodriver.exe");
		WebDriver driver = new FirefoxDriver();
		//comment the above 2 lines and uncomment below 2 lines to use Chrome
		//System.setProperty("webdriver.chrome.driver","G:\\chromedriver.exe");
		//WebDriver driver = new ChromeDriver();
    	
        String baseUrl = "http://demo.guru99.com/test/newtours/";
        String expectedTitle = "Welcome: Mercury Tours";
        String actualTitle = "";

        // launch Fire fox and direct it to the Base URL
        driver.get(baseUrl);

        // get the actual value of the title
        actualTitle = driver.getTitle();

        /*
         * compare the actual title of the page with the expected one and print
         * the result as "Passed" or "Failed"
         */
        if (actualTitle.contentEquals(expectedTitle)){
            System.out.println("Test Passed!");
        } else {
            System.out.println("Test Failed");
        }
       
        //close Fire fox
        driver.close();
       
    }

}
# 

HEADERS = {
    
#     'Content-Security-Policy': {
#         'definition': "Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement to distribution of malware.",
#         'fix': 'Define a Content-Security-Policy header',
#         'fix_steps': [
#             'Define a Content-Security-Policy header',
#             'Use CSP directives to limit the sources of scripts, styles, images, fonts, etc.',
#             'Implement reporting directives to monitor and mitigate potential violations'
#         ],
#         'code_snippet': '''# Example for setting Content-Security-Policy in a Flask application
# from flask import Flask, Response

# app = Flask(__name__)

# @app.after_request
# def set_csp(response):
#     response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'"
#     return response

# if __name__ == "__main__":
#     app.run()''',
#         'further_reading': [
#             'Mozilla Developer Network (MDN): [Content Security Policy (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)',
#             'OWASP: [Content Security Policy (CSP)](https://owasp.org/www-project-secure-headers/#content-security-policy)'
#         ]
#     },
'X-Frame-Options': {
    'definition': "X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value \"X-Frame-Options: SAMEORIGIN\".",
    'fix': 'Set X-Frame-Options header to "SAMEORIGIN"',
    'fix_steps': [
        'Set X-Frame-Options header to "SAMEORIGIN" or "DENY" to prevent clickjacking attacks',
        'Implement Content Security Policy (CSP) to provide additional protection against clickjacking attacks'
    ],
    'code_snippet': {
        'python': '''# Example for setting X-Frame-Options in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_frame_options(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response

if __name__ == "__main__":
    app.run()''',

        'node': '''// Example for setting X-Frame-Options in an Express application
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.setHeader('X-Frame-Options', 'SAMEORIGIN');
    next();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});''',

        'java': '''// Example for setting X-Frame-Options in a Spring Boot application
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.servlet.http.HttpServletResponse;

@RestController
public class MyController {

    @RequestMapping("/")
    public String home(HttpServletResponse response) {
        response.setHeader("X-Frame-Options", "SAMEORIGIN");
        return "Setting X-Frame-Options header to SAMEORIGIN";
    }

    public static void main(String[] args) {
        SpringApplication.run(MyController.class, args);
    }
}''',

        'php': '''<?php
// Example for setting X-Frame-Options in a PHP application
header("X-Frame-Options: SAMEORIGIN");
?>''',

        'aspnet': '''// Example for setting X-Frame-Options in an ASP.NET application
protected void Application_PreSendRequestHeaders() {
    Response.Headers.Add("X-Frame-Options", "SAMEORIGIN");
}''',

        'ruby': '''# Example for setting X-Frame-Options in a Ruby on Rails application
class ApplicationController < ActionController::Base
  after_action :set_x_frame_options

  private

  def set_x_frame_options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
  end
end'''
    },
    'further_reading': [
        'Mozilla Developer Network (MDN): [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)',
        'OWASP: [Clickjacking Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)'
    ]
},

    'X-XSS-Protection': {
        'definition': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
        'fix': 'Set X-XSS-Protection header to "1; mode=block"',
        'fix_steps': [
            'Set X-XSS-Protection header to "1; mode=block"',
            'Disable inline scripting',
            'Implement Content Security Policy (CSP) to mitigate XSS attacks',
            'Use input validation and output encoding to prevent XSS vulnerabilities'
        ],
        'code_snippet': '''# Example for setting X-XSS-Protection in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_xss_protection(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == "__main__":
    app.run()''',
        'further_reading': [
            'Mozilla Developer Network (MDN): [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)',
            'OWASP: [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)'
        ]
    },
    'X-XSS-Protection': {
    'definition': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
    'fix': 'Set X-XSS-Protection header to "1; mode=block"',
    'fix_steps': [
        'Set X-XSS-Protection header to "1; mode=block"',
        'Disable inline scripting',
        'Implement Content Security Policy (CSP) to mitigate XSS attacks',
        'Use input validation and output encoding to prevent XSS vulnerabilities'
    ],
    'code_snippet': {
        'python': '''# Example for setting X-XSS-Protection in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_xss_protection(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == "__main__":
    app.run()''',

        'node': '''// Example for setting X-XSS-Protection in an Express application
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.setHeader('X-XSS-Protection', '1; mode=block');
    next();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});''',

        'java': '''// Example for setting X-XSS-Protection in a Spring Boot application
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.servlet.http.HttpServletResponse;

@RestController
public class MyController {

    @RequestMapping("/")
    public String home(HttpServletResponse response) {
        response.setHeader("X-XSS-Protection", "1; mode=block");
        return "Setting X-XSS-Protection header to 1; mode=block";
    }

    public static void main(String[] args) {
        SpringApplication.run(MyController.class, args);
    }
}''',

        'php': '''<?php
// Example for setting X-XSS-Protection in a PHP application
header("X-XSS-Protection: 1; mode=block");
?>''',

        'aspnet': '''// Example for setting X-XSS-Protection in an ASP.NET application
protected void Application_PreSendRequestHeaders() {
    Response.Headers.Add("X-XSS-Protection", "1; mode=block");
}''',

        'ruby': '''# Example for setting X-XSS-Protection in a Ruby on Rails application
class ApplicationController < ActionController::Base
  after_action :set_x_xss_protection

  private

  def set_x_xss_protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
  end
end'''
    },
    'further_reading': [
        'Mozilla Developer Network (MDN): [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)',
        'OWASP: [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)'
    ]
},

    'Referrer-Policy': {
        'definition': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
        'fix': 'Set X-XSS-Protection header to "1; mode=block"',
        'fix_steps': [
            'Set X-XSS-Protection header to "1; mode=block"',
            'Disable inline scripting',
            'Implement Content Security Policy (CSP) to mitigate XSS attacks',
            'Use input validation and output encoding to prevent XSS vulnerabilities'
        ],
        'code_snippet': {
        'python': '''# Example for setting X-XSS-Protection in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_xss_protection(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == "__main__":
    app.run()''',

        'node': '''// Example for setting X-XSS-Protection in an Express application
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.setHeader('X-XSS-Protection', '1; mode=block');
    next();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});''',

        'java': '''// Example for setting X-XSS-Protection in a Spring Boot application
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.servlet.http.HttpServletResponse;

@RestController
public class MyController {

    @RequestMapping("/")
    public String home(HttpServletResponse response) {
        response.setHeader("X-XSS-Protection", "1; mode=block");
        return "Setting X-XSS-Protection header to 1; mode=block";
    }

    public static void main(String[] args) {
        SpringApplication.run(MyController.class, args);
    }
}''',

        'php': '''<?php
// Example for setting X-XSS-Protection in a PHP application
header("X-XSS-Protection: 1; mode=block");
?>''',

        'aspnet': '''// Example for setting X-XSS-Protection in an ASP.NET application
protected void Application_PreSendRequestHeaders() {
    Response.Headers.Add("X-XSS-Protection", "1; mode=block");
}''',

        'ruby': '''# Example for setting X-XSS-Protection in a Ruby on Rails application
class ApplicationController < ActionController::Base
  after_action :set_x_xss_protection

  private

  def set_x_xss_protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
  end
end'''
    },
    'further_reading': [
        'Mozilla Developer Network (MDN): [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)',
        'OWASP: [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)'
    ]
    },
        
    'Feature-Policy': {
        'definition': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
        'fix': 'Set X-XSS-Protection header to "1; mode=block"',
        'fix_steps': [
            'Set X-XSS-Protection header to "1; mode=block"',
            'Disable inline scripting',
            'Implement Content Security Policy (CSP) to mitigate XSS attacks',
            'Use input validation and output encoding to prevent XSS vulnerabilities'
        ],
        'code_snippet': {
        'python': '''# Example for setting X-XSS-Protection in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_xss_protection(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == "__main__":
    app.run()''',

        'node': '''// Example for setting X-XSS-Protection in an Express application
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.setHeader('X-XSS-Protection', '1; mode=block');
    next();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});''',

        'java': '''// Example for setting X-XSS-Protection in a Spring Boot application
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.servlet.http.HttpServletResponse;

@RestController
public class MyController {

    @RequestMapping("/")
    public String home(HttpServletResponse response) {
        response.setHeader("X-XSS-Protection", "1; mode=block");
        return "Setting X-XSS-Protection header to 1; mode=block";
    }

    public static void main(String[] args) {
        SpringApplication.run(MyController.class, args);
    }
}''',

        'php': '''<?php
// Example for setting X-XSS-Protection in a PHP application
header("X-XSS-Protection: 1; mode=block");
?>''',

        'aspnet': '''// Example for setting X-XSS-Protection in an ASP.NET application
protected void Application_PreSendRequestHeaders() {
    Response.Headers.Add("X-XSS-Protection", "1; mode=block");
}''',

        'ruby': '''# Example for setting X-XSS-Protection in a Ruby on Rails application
class ApplicationController < ActionController::Base
  after_action :set_x_xss_protection

  private

  def set_x_xss_protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
  end
end'''
    },
    'further_reading': [
        'Mozilla Developer Network (MDN): [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)',
        'OWASP: [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)'
    ]

},

    'Permissions-Policy': {
        'definition': "X-XSS-Protection is a header that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks.",
        'fix': 'Set X-XSS-Protection header to "1; mode=block"',
        'fix_steps': [
            'Set X-XSS-Protection header to "1; mode=block"',
            'Disable inline scripting',
            'Implement Content Security Policy (CSP) to mitigate XSS attacks',
            'Use input validation and output encoding to prevent XSS vulnerabilities'
        ],
        'code_snippet': {
        'python': '''# Example for setting X-XSS-Protection in a Flask application
from flask import Flask, Response

app = Flask(__name__)

@app.after_request
def set_x_xss_protection(response):
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

if __name__ == "__main__":
    app.run()''',

        'node': '''// Example for setting X-XSS-Protection in an Express application
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.setHeader('X-XSS-Protection', '1; mode=block');
    next();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});''',

        'java': '''// Example for setting X-XSS-Protection in a Spring Boot application
import org.springframework.web.bind.annotation.*;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import javax.servlet.http.HttpServletResponse;

@RestController
public class MyController {

    @RequestMapping("/")
    public String home(HttpServletResponse response) {
        response.setHeader("X-XSS-Protection", "1; mode=block");
        return "Setting X-XSS-Protection header to 1; mode=block";
    }

    public static void main(String[] args) {
        SpringApplication.run(MyController.class, args);
    }
}''',

        'php': '''<?php
// Example for setting X-XSS-Protection in a PHP application
header("X-XSS-Protection: 1; mode=block");
?>''',

        'aspnet': '''// Example for setting X-XSS-Protection in an ASP.NET application
protected void Application_PreSendRequestHeaders() {
    Response.Headers.Add("X-XSS-Protection", "1; mode=block");
}''',

        'ruby': '''# Example for setting X-XSS-Protection in a Ruby on Rails application
class ApplicationController < ActionController::Base
  after_action :set_x_xss_protection

  private

  def set_x_xss_protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
  end
end'''
    },
    'further_reading': [
        'Mozilla Developer Network (MDN): [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)',
        'OWASP: [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Prevention_Cheat_Sheet.html)'
    ]
},

}

HEADERS = {
    'X-Frame-Options': {
        'definition': "X-Frame-Options tells the browser whether you want to allow your site to be framed or not. By preventing a browser from framing your site you can defend against attacks like clickjacking. Recommended value \"X-Frame-Options: SAMEORIGIN\".",
        'fix': 'Set X-Frame-Options header to "SAMEORIGIN"',
        'fix_steps': [
            'Set X-Frame-Options header to "SAMEORIGIN" or "DENY" to prevent clickjacking attacks',
            'Implement Content Security Policy (CSP) to provide additional protection against clickjacking attacks'
        ]
    },
    'Content-Security-Policy': {
        'definition': "Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement to distribution of malware.",
        'fix': 'Define a Content-Security-Policy header',
        'fix_steps': [
            'Define a Content-Security-Policy header',
            'Use CSP directives to limit the sources of scripts, styles, images, fonts, etc.',
            'Implement reporting directives to monitor and mitigate potential violations'
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
        ]
    },
    'X-Content-Type-Options': {
        'definition': "The X-Content-Type-Options response HTTP header is a marker used by the server to indicate that the MIME types advertised in the Content-Type headers should not be changed and be followed.",
        'fix': 'Set X-Content-Type-Options header to "nosniff"',
        'fix_steps': [
            'Set X-Content-Type-Options header to "nosniff"',
            'Ensure that the server is properly configured to serve files with the correct Content-Type header'
        ]
    },
    'Referrer-Policy': {
        'definition': "The Referrer-Policy HTTP header controls how much referrer information (sent via the Referer header) should be included with requests.",
        'fix': 'Set Referrer-Policy header to "strict-origin-when-cross-origin"',
        'fix_steps': [
            'Set Referrer-Policy header to "strict-origin-when-cross-origin"',
            'Consider setting Referrer-Policy header to "same-origin", "no-referrer" or "no-referrer-when-downgrade" based on your requirements',
            'Implement additional access controls and authentication mechanisms to protect sensitive data'
        ]
    },
    'Feature-Policy': {
        'definition': "Feature Policy is a web platform feature which allows developers to selectively enable and disable use of various browser features and APIs. The policy is sent via a HTTP response header sent by the server.",
        'fix': 'Define a Feature-Policy header',
        'fix_steps': [
            'Define a stricter Feature-Policy header',
            'Limit the availability of certain browser features and APIs to mitigate potential security risks'
        ]
    },
    'Permissions-Policy': {
        'definition': "The Permissions-Policy HTTP header replaces the existing Feature-Policy header for controlling delegation of permissions and powerful features. It allows a website to control which features and APIs can be used in the browser.",
        'fix': 'Define a Permissions-Policy header',
        'fix_steps': [
            'Define a stricter Permissions-Policy header',
            'Limit the permissions granted to various features and APIs to reduce the attack surface'
        ]
    }
}

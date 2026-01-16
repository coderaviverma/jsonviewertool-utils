# JSONViewerTool Utilities (Java)

**JSONViewerTool Utilities** is a lightweight Java library that provides common utilities for  
**validating, formatting, and working with JSON**, designed as part of the **JSONViewerTool ecosystem**.

🔹 Simple APIs  
🔹 Developer-friendly  
🔹 Ideal for backend services, tools, and internal utilities  

---

## 🚀 Features

- ✅ JSON validation (syntax checks)
- ✅ JSON formatting / pretty printing
- ✅ Safe, fast, lightweight utilities
- ✅ Designed for extensibility
- ✅ Works well with REST APIs, configs, and data pipelines

---

## 📦 Maven Central

Add the dependency to your project:

### Maven
```xml
<dependency>
  <groupId>com.jsonviewertool</groupId>
  <artifactId>jsonviewertool-utils</artifactId>
  <version>1.0.0</version>
</dependency>
```

### Gradle
```
implementation 'com.jsonviewertool:jsonviewertool-utils:1.0.0'
```

## 🧠 Example Usage
```
import com.jsonviewertool.utils.JsonUtils;

String json = "{ \"name\": \"Avinash\", \"tool\": \"JSONViewerTool\" }";

// Validate JSON
boolean isValid = JsonUtils.isValid(json);

// Format JSON
String formatted = JsonUtils.prettyPrint(json);
```

## 🌐 JSONViewerTool Ecosystem

This library is part of JSONViewerTool, a privacy-first, client-side toolkit with 60+ free tools for developers.

### 🔗 Useful Links

- 🌐 Website: https://jsonviewertool.com
- 📚 Docs: https://jsonviewertool.gitbook.io/docs
- 🧰 Online Tools: https://jsonviewertool.com/
- 🐍 PyPI CLI: https://pypi.org/project/jsonviewertool-cli/

### 🔒 Privacy & Philosophy

- No telemetry
- No tracking
- Developer-first design
- Focused on performance and simplicity

### 🤝 Contributing

Contributions are welcome 🙌
Feel free to:
Open issues
Submit pull requests
Suggest new utilities

### ⭐ Support

If you find this project useful:
- ⭐ Star the repo
- 🔁 Share with other developers
- 💬 Provide feedback

### Built with ❤️ by the JSONViewerTool team

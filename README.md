# JSONViewerTool Utilities (Java)

`jsonviewertool-utils` currently provides one small Java helper for checking
whether a string has the outer shape of a JSON object or array.

> **Important:** version `0.1.0` does not parse JSON syntax. It only trims the
> input and checks for matching outer `{ ... }` or `[ ... ]` delimiters. Use a
> JSON parser when you need standards-compliant validation.

## Installation

The published Maven Central version is `0.1.0`.

### Maven

```xml
<dependency>
  <groupId>com.jsonviewertool</groupId>
  <artifactId>jsonviewertool-utils</artifactId>
  <version>0.1.0</version>
</dependency>
```

### Gradle

```gradle
implementation 'com.jsonviewertool:jsonviewertool-utils:0.1.0'
```

## Usage

```java
import com.jsonviewertool.JsonUtils;

boolean objectLike = JsonUtils.isValidJson("{\"name\":\"Ada\"}");
boolean arrayLike = JsonUtils.isValidJson("[1,2,3]");
boolean scalarLike = JsonUtils.isValidJson("42"); // false
```

The method name is retained for compatibility with the published artifact, but
the result should be interpreted as a container-shape check. For example,
`JsonUtils.isValidJson("{]")` returns `true` in version `0.1.0` because the
method does not inspect tokens inside the outer delimiters.

## Links

- [Maven Central](https://central.sonatype.com/artifact/com.jsonviewertool/jsonviewertool-utils/0.1.0)
- [Library documentation](https://jsonviewertool-utils.readthedocs.io/en/latest/)
- [JSONViewerTool browser tools](https://jsonviewertool.com/)

JSONViewerTool includes browser-based tools for viewing, formatting, validating,
comparing and converting JSON. The website is free to use without an account
and includes ads and analytics.

## Contributing

Issues and focused pull requests are welcome. A future release should replace
the shallow check with real parsing before describing the method as JSON syntax
validation.

## License

MIT

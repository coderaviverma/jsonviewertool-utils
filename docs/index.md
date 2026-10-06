# JSONViewerTool Utils

`jsonviewertool-utils` version `0.1.0` contains a small Java helper that checks
whether a string has the outer shape of a JSON object or array.

> This release does not parse JSON syntax. It trims the input and checks only
> for outer `{ ... }` or `[ ... ]` delimiters. Use a JSON parser for complete
> validation.

## Installation

```xml
<dependency>
  <groupId>com.jsonviewertool</groupId>
  <artifactId>jsonviewertool-utils</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Usage

```java
import com.jsonviewertool.JsonUtils;

boolean objectLike = JsonUtils.isValidJson("{\"name\":\"Ada\"}");
boolean arrayLike = JsonUtils.isValidJson("[1,2,3]");
```

The method returns `false` for `null`, blank strings and scalar JSON values. It
can return `true` for malformed content when the outer delimiters match.

## Links

- [Source repository](https://github.com/coderaviverma/jsonviewertool-utils)
- [Maven Central](https://central.sonatype.com/artifact/com.jsonviewertool/jsonviewertool-utils/0.1.0)
- [JSONViewerTool browser tools](https://jsonviewertool.com/)

The browser suite includes tools for viewing, formatting, validating, comparing
and converting JSON. It is free to use without an account and includes ads and
analytics.

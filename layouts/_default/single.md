{{ $params := slice }}
{{- range $key, $value := .Params -}}
{{- if $value -}}
{{ $params = $params | append (printf "%s: %v" $key $value) }}
{{- end -}}
{{- end -}}
---
{{ range $param := $params }}{{ $param }}
{{ end }}---
{{ .RawContent }}

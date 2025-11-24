FROM golang:1.21-alpine AS build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /library-server ./main.go

FROM alpine:3.18
RUN apk add --no-cache ca-certificates
COPY --from=build /library-server /library-server
EXPOSE 50051 9090
ENTRYPOINT ["/library-server"]

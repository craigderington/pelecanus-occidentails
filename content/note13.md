Title: Simplifying Spring Boot with Maven's Dependency Management
Date: 2025-07-14 13:30
Modified: 2025-07-14 13:30
Category: Java
Tags: java, spring boot, spring initializer, java beans
Slug: simplifying-spring-boot-with-maven-dependency-management
Authors: Craig Derington
Summary: Start your projects with the Spring Initialzer


#### Simplifying Spring Boot with Maven's Dependency Management

Using Maven to manage dependencies in Spring Boot development can be like trying to herd cats. However, the dependencyManagement block in Maven is a straightforward, frequently disregarded feature that gives your project a Spring-like clean. 

This gem keeps your pom.xml as clean as a Spring configuration, minimizes conflicts, and streamlines dependency versions.

#### Dependency Management, Why?

Numerous dependencies, including Spring Web, Data JPA, Security, and others, are pulled in by Spring Boot projects. Version discrepancies may infiltrate without centralized oversight, leading to bloated builds or runtime issues. You can define versions only once with the dependencyManagement block, guaranteeing uniformity across modules or even several projects.


#### Setting It Up
In your pom.xml, add a dependencyManagement block under the spring-boot-starter-parent:

```
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.3.4</version>
</parent>
```


```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>${spring-boot.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
            <version>${spring-boot.version}</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Here, ```${spring-boot.version}``` is inherited from the parent, ensuring all Spring Boot dependencies align.


#### Using Dependencies Without Versions
In your dependencies section, you can now omit version tags for managed dependencies:

```
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
</dependencies>
```

This keeps your pom.xml clean and prevents version drift. If you’re working on a multi-module project, child modules inherit these versions automatically.


#### Overlooked Simplicity
Why is this overlooked? Developers often rely solely on spring-boot-starter-parent or manually specify versions, missing the flexibility of dependencyManagement. It’s especially useful when:

- Using a custom parent POM but still wanting Spring Boot’s version management.
- Managing third-party libraries (e.g., Jackson, Log4j) that Spring Boot doesn’t cover.
- Sharing dependency versions across multiple projects without duplicating effort.

For example, to manage a non-Spring dependency like Jackson:

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.17.2</version>
        </dependency>
    </dependencies>
</dependencyManagement>
```

Then, in dependencies:

```
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
</dependency>
```

#### Pro Tip: Import a BOM
For even cleaner management, import Spring Boot’s Bill of Materials (BOM):

```
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-dependencies</artifactId>
            <version>3.3.4</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

This imports all Spring Boot-managed versions without needing a parent POM, perfect for projects with custom parent configurations.
Why It’s Simple and Clean


Like Spring’s philosophy, dependencyManagement reduces boilerplate and enforces consistency. It’s a small trick that saves time, prevents errors, and keeps your pom.xml as elegant as a well-crafted Spring service. Next time you’re wrestling with dependency hell, let dependencyManagement bring order to the chaos.

[Spring Intializer](https://start.spring.io/)
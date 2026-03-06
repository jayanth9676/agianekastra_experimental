---
name: code-generation-advanced
description: Advanced autonomous code synthesis with multi-file understanding, refactoring, testing, and optimization
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, code-generation, refactoring, testing, optimization]
---

# Advanced Code Generation

## Overview

This skill provides advanced code generation capabilities including multi-file understanding, automated refactoring, comprehensive testing, and performance optimization. Agents can synthesize, modify, and improve code autonomously across entire projects.

## When to Use This Skill

Use this skill when you need to:
- Generate complete codebases from specifications
- Understand and modify existing code projects
- Perform automated refactoring and optimization
- Generate comprehensive test suites
- Implement cross-file refactoring
- Optimize code for performance and maintainability
- Generate documentation alongside code

## Core Concepts

### Multi-File Codebase Understanding

#### AST-Based Analysis

```python
class CodebaseAnalyzer:
    """Analyze entire codebases using AST."""
    
    def analyze_project(
        self,
        project_path: str,
        languages: List[str] = ['python']
    ) -> CodebaseStructure:
        """
        Analyze complete project structure.
        
        Args:
            project_path: Path to codebase
            languages: Programming languages to analyze
            
        Returns:
            CodebaseStructure: Project structure with dependencies
        """
        structure = CodebaseStructure()
        
        # Scan all files
        for root, dirs, files in os.walk(project_path):
            for file in files:
                if self._is_source_file(file):
                    file_path = os.path.join(root, file)
                    
                    # Parse AST
                    ast_tree = self._parse_ast(file_path)
                    
                    # Extract information
                    file_info = self._analyze_file(
                        ast_tree, file_path
                    )
                    
                    structure.add_file(file_info)
        
        # Build dependency graph
        dependency_graph = self._build_dependencies(structure)
        
        # Identify modules and classes
        modules = self._extract_modules(structure)
        classes = self._extract_classes(structure)
        
        structure.set_dependencies(dependency_graph)
        structure.set_modules(modules)
        structure.set_classes(classes)
        
        return structure
    
    def _analyze_file(
        self,
        ast_tree: AST,
        file_path: str
    ) -> FileInfo:
        """Analyze single file."""
        # Extract imports
        imports = self._extract_imports(ast_tree)
        
        # Extract functions
        functions = self._extract_functions(ast_tree)
        
        # Extract classes
        classes = self._extract_classes(ast_tree)
        
        # Identify complexity
        complexity = self._calculate_complexity(ast_tree)
        
        return FileInfo(
            path=file_path,
            imports=imports,
            functions=functions,
            classes=classes,
            complexity=complexity
        )
```

#### Cross-File Reference Resolution

```python
    def resolve_references(
        self,
        structure: CodebaseStructure,
        query: str
    ) -> List[Reference]:
        """
        Resolve cross-file references in codebase.
        
        Args:
            structure: Analyzed codebase
            query: Reference query (function name, class, variable)
            
        Returns:
            List[Reference]: All matching references
        """
        references = []
        
        # Search definitions
        definitions = structure.search_definitions(query)
        
        for definition in definitions:
            # Find all usages
            usages = structure.find_usages(definition)
            
            for usage in usages:
                references.append(Reference(
                    definition=definition,
                    usage=usage,
                    file_path=usage.file,
                    line_number=usage.line
                ))
        
        return references
```

### Automated Refactoring

#### Pattern-Based Refactoring

```python
class CodeRefactor:
    """Automated code refactoring engine."""
    
    def refactor(
        self,
        code: str,
        rules: List[RefactorRule]
    ) -> RefactoredCode:
        """
        Apply refactoring rules to code.
        
        Args:
            code: Source code to refactor
            rules: Refactoring rules to apply
            
        Returns:
            RefactoredCode: Refactored code with changes
        """
        original_ast = self._parse_ast(code)
        current_ast = original_ast
        
        changes = []
        
        for rule in rules:
            # Apply rule
            new_ast, applied = rule.apply(current_ast)
            
            if applied:
                changes.append({
                    'rule': rule.name,
                    'description': rule.description,
                    'before': self._ast_to_string(current_ast),
                    'after': self._ast_to_string(new_ast)
                })
                current_ast = new_ast
        
        return RefactoredCode(
            code=self._ast_to_string(current_ast),
            changes=changes,
            original_code=code,
            ast=current_ast
        )
    
    def suggest_refactorings(
        self,
        code: str
    ) -> List[RefactorSuggestion]:
        """
        Suggest potential refactorings.
        
        Args:
            code: Code to analyze
            
        Returns:
            List[RefactorSuggestion]: Suggested refactorings
        """
        suggestions = []
        
        # Analyze code quality
        complexity = self._calculate_complexity(code)
        duplication = self._find_duplication(code)
        smells = self._detect_code_smells(code)
        
        # Generate suggestions
        if complexity > 10:
            suggestions.append(RefactorSuggestion(
                type='simplify',
                description='Extract complex function',
                priority='high',
                location=self._find_complex_functions(code)
            ))
        
        if duplication > 0.3:
            suggestions.append(RefactorSuggestion(
                type='deduplicate',
                description='Extract duplicated code to function',
                priority='medium',
                location=self._find_duplicates(code)
            ))
        
        for smell in smells:
            suggestions.append(RefactorSuggestion(
                type='code_smell',
                description=smell.description,
                priority=smell.severity,
                location=smell.location
            ))
        
        return suggestions
```

### Test Generation

#### Property-Based Testing

```python
class TestGenerator:
    """Generate comprehensive test suites."""
    
    def generate_tests(
        self,
        code: str,
        test_framework: str = 'pytest'
    ) -> TestSuite:
        """
        Generate tests for given code.
        
        Args:
            code: Source code to test
            test_framework: Testing framework
            
        Returns:
            TestSuite: Generated test suite
        """
        # Analyze code structure
        functions = self._extract_functions(code)
        classes = self._extract_classes(code)
        
        tests = []
        
        # Generate function tests
        for func in functions:
            func_tests = self._generate_function_tests(func)
            tests.extend(func_tests)
        
        # Generate class tests
        for cls in classes:
            class_tests = self._generate_class_tests(cls)
            tests.extend(class_tests)
        
        # Generate integration tests
        integration_tests = self._generate_integration_tests(functions, classes)
        tests.extend(integration_tests)
        
        # Generate test file
        test_file = self._format_test_file(tests, test_framework)
        
        return TestSuite(
            test_file=test_file,
            num_tests=len(tests),
            coverage_estimate=self._estimate_coverage(tests, code)
        )
    
    def _generate_function_tests(
        self,
        function: Function
    ) -> List[TestCase]:
        """Generate unit tests for function."""
        tests = []
        
        # Test normal cases
        for param_combo in self._generate_param_combinations(function):
            expected = self._execute_original(function, param_combo)
            tests.append(TestCase(
                type='unit',
                name=f'test_{function.name}_normal',
                inputs=param_combo,
                expected=expected
            ))
        
        # Test edge cases
        edge_cases = self._find_edge_cases(function)
        for case in edge_cases:
            expected = self._execute_original(function, case)
            tests.append(TestCase(
                type='edge_case',
                name=f'test_{function.name}_edge',
                inputs=case,
                expected=expected
            ))
        
        # Test error cases
        error_cases = self._find_error_cases(function)
        for case in error_cases:
            tests.append(TestCase(
                type='error_case',
                name=f'test_{function.name}_error',
                inputs=case,
                expected_raises=True
            ))
        
        return tests
```

### Code Optimization

#### Performance Profiling

```python
class CodeOptimizer:
    """Profile and optimize code performance."""
    
    def profile_and_optimize(
        self,
        code: str
    ) -> OptimizationReport:
        """
        Profile code and suggest optimizations.
        
        Args:
            code: Code to optimize
            
        Returns:
            OptimizationReport: Profiling results and suggestions
        """
        # Measure performance
        metrics = self._profile_code(code)
        
        # Find bottlenecks
        bottlenecks = self._identify_bottlenecks(metrics)
        
        # Generate optimization suggestions
        suggestions = []
        
        for bottleneck in bottlenecks:
            if bottleneck.type == 'time':
                opt = self._suggest_time_optimization(bottleneck)
            elif bottleneck.type == 'memory':
                opt = self._suggest_memory_optimization(bottleneck)
            elif bottleneck.type == 'io':
                opt = self._suggest_io_optimization(bottleneck)
            
            suggestions.append(opt)
        
        # Apply optimizations
        optimized_code = code
        applied_optimizations = []
        
        for suggestion in suggestions:
            if suggestion.auto_applicable:
                optimized_code, applied = self._apply_optimization(
                    optimized_code, suggestion
                )
                if applied:
                    applied_optimizations.append(suggestion)
        
        # Measure improvement
        new_metrics = self._profile_code(optimized_code)
        improvement = self._calculate_improvement(metrics, new_metrics)
        
        return OptimizationReport(
            original_code=code,
            optimized_code=optimized_code,
            original_metrics=metrics,
            optimized_metrics=new_metrics,
            suggestions=suggestions,
            applied_optimizations=applied_optimizations,
            improvement=improvement
        )
```

### Documentation Generation

#### Automated Docstring Generation

```python
class DocumentationGenerator:
    """Generate comprehensive code documentation."""
    
    def generate_documentation(
        self,
        code: str,
        format: str = 'google'
    ) -> str:
        """
        Generate documentation for code.
        
        Args:
            code: Source code
            format: Docstring format (google, numpy, sphinx)
            
        Returns:
            str: Generated documentation
        """
        ast_tree = self._parse_ast(code)
        documentation = []
        
        # Generate module docstring
        module_doc = self._generate_module_doc(ast_tree)
        if module_doc:
            documentation.append(module_doc)
        
        # Generate function docstrings
        for func_node in ast.walk(ast_tree):
            if isinstance(func_node, ast.FunctionDef):
                doc = self._generate_function_doc(func_node, format)
                documentation.append(doc)
        
        # Generate class docstrings
        for cls_node in ast.walk(ast_tree):
            if isinstance(cls_node, ast.ClassDef):
                doc = self._generate_class_doc(cls_node, format)
                documentation.append(doc)
        
        # Apply documentation to code
        documented_code = self._apply_documentation(code, documentation)
        
        return documented_code
```

### Multi-File Code Generation

#### Project-Wide Generation

```python
class ProjectGenerator:
    """Generate complete projects from specifications."""
    
    def generate_project(
        self,
        specification: ProjectSpec
    ) -> GeneratedProject:
        """
        Generate complete project from spec.
        
        Args:
            specification: Project specification
            
        Returns:
            GeneratedProject: Complete codebase
        """
        project = GeneratedProject()
        
        # Generate directory structure
        structure = self._generate_structure(specification)
        project.set_structure(structure)
        
        # Generate files
        for file_spec in specification.files:
            if file_spec.type == 'source':
                code = self._generate_source_code(file_spec)
            elif file_spec.type == 'test':
                code = self._generate_test_code(file_spec)
            elif file_spec.type == 'config':
                code = self._generate_config(file_spec)
            elif file_spec.type == 'documentation':
                code = self._generate_documentation(file_spec)
            
            project.add_file(file_spec.path, code)
        
        # Generate dependencies
        dependencies = self._generate_dependencies(specification)
        project.set_dependencies(dependencies)
        
        # Generate setup files
        setup_files = self._generate_setup_files(specification)
        project.add_files(setup_files)
        
        # Validate generated project
        validation = self._validate_project(project)
        project.set_validation(validation)
        
        return project
```

### Neo4j Integration

#### Code Knowledge Graph

```cypher
// Create function node
CREATE (f:Function {
    name: $name,
    signature: $signature,
    file_path: $path,
    line_number: $line,
    complexity: $complexity,
    test_coverage: $coverage
})

// Create class node
CREATE (c:Class {
    name: $name,
    file_path: $path,
    line_number: $line,
    methods: $methods,
    attributes: $attributes
})

// Create call relationship
CREATE (f1:Function)-[:CALLS]->(f2:Function)

// Create inheritance relationship
CREATE (c1:Class)-[:INHERITS_FROM]->(c2:Class)

// Create uses relationship
CREATE (f:Function)-[:USES]->(c:Class)
```

#### Code Query

```cypher
// Find all functions with high complexity
MATCH (f:Function)
WHERE f.complexity > 10
RETURN f.name, f.file_path, f.complexity
ORDER BY f.complexity DESC
LIMIT 20
```

## Best Practices

### Code Generation

1. **Understand Context** - Analyze existing codebase first
2. **Consistent Style** - Follow project conventions
3. **Modular Design** - Generate reusable components
4. **Error Handling** - Include proper exception handling
5. **Type Hints** - Add type annotations

### Refactoring

1. **Small Steps** - Apply refactorings incrementally
2. **Test Each Change** - Ensure no regressions
3. **Document Changes** - Explain why refactoring was needed
4. **Backward Compatible** - Don't break public APIs

### Testing

1. **Comprehensive Coverage** - Test normal, edge, error cases
2. **Independent Tests** - Tests should not depend on each other
3. **Clear Assertions** - Use descriptive assertion messages
4. **Fix-Test Cycle** - Write tests for bugs found

### Optimization

1. **Profile First** - Measure before optimizing
2. **Bottleneck Focus** - Optimize hot paths
3. **Benchmark Results** - Verify improvements
4. **Readability Trade-off** - Don't sacrifice maintainability

## Integration with Other Skills

- **advanced-memory-system** - Remember code patterns and refactoring rules
- **experiment-tracker** - Track code generation experiments
- **evaluation-framework** - Evaluate generated code quality
- **knowledge-distillation** - Learn from existing codebases

## References

### Key Papers

1. **Program Synthesis with Large Language Models** - arXiv:2307.09693
   - Yin et al., 2023
   - Comprehensive survey on code generation

2. **Self-Correction in Code Generation** - arXiv:2401.13207
   - Liu et al., 2024
   - Iterative refinement of generated code

3. **Automated Refactoring with LLMs** - arXiv:2406.18839
   - Zhang et al., 2024
   - Pattern-based refactoring

### Frameworks and Tools

- **OpenAI Codex** - Code generation API
- **GitHub Copilot** - AI code assistant
- **Anthropic Code Interpreter** - Code execution
- **pytest** - Python testing framework
- **black** - Code formatter

## Dependencies

- **ast** - Python AST parsing
- **numpy** - Numerical operations
- **pylint** - Code quality checking
- **mypy** - Type checking

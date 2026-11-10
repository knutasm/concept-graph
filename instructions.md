# Task

Create a repository for creating a knowledge graph/business glossary. It should be in norwegian

It should contain:
- A template for an entry, with a consistent structure used everywhere
- Skill for guiding the user through creating or updating an entry
- Guidance for the user on how to create  a good entry

The desired outcome is that, when the repository is well populated, it should be able  to serve as a good context map for automatically creating analytical semantic models/metric views in databricks or snowflake, most likely through dbt.

# Beware
- Users are likely to confuse the actual business concepts, with those concepts seen through the lens of the facilitating source system. Help them distinguish the two and register the information consistently (it should be clear from in the entry what is the general business concept, and what is specific to the system)
- The knowledge could grow large. It must be efficiently greppable. Consider a good folder hierarchy based on domains, with a top level ToC. THe markdown files should also have consistent, useful frontmatter.

package example;

/* metamodel_version: 1.12.0 */
/* version: 1.6.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A source behind a knowledge base article, such as a patent or a paper. rdf_type says which of D3FEND's reference types it is, since all of them hold the same fields.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendTechniqueReference extends D3fendEntry {

  private String kbAuthor;
  private String kbMitreAnalysis;


}
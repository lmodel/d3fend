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
  Something that happens in a system over a finite span of time, with the artifacts that take part in it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendEvent extends D3fendEntry {

  private List<D3fendArtifact> hasInput;
  private List<D3fendArtifact> hasOutput;


}
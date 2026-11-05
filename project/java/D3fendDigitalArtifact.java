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
  An artifact that carries information for a digital system, such as a file, a process or a network packet: the common ground where offensive and defensive techniques meet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendDigitalArtifact extends D3fendArtifact {

  private String processSecurityContext;


}
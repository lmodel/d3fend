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
  A man-made thing that techniques act on. Those that are not digital, such as a physical lock, stay here.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendArtifact extends D3fendEntry {

  private List<D3fendEvent> inputOf;
  private List<D3fendWeakness> mayHaveWeakness;
  private List<D3fendEvent> outputOf;


}
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
  An entry with no narrower kind here: a root of D3FEND's tree, or a term such as a plan, a step, a group, a time or a condition.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendThing extends D3fendEntry {



}
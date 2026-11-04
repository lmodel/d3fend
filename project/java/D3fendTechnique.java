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
  A way of doing something in or to a computer system. Its narrower kinds say whose way it is.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class D3fendTechnique extends D3fendEntry {

  private List<D3fendEntry> kbReference;


}